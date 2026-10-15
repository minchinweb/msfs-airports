"""Straighten the 2019 aerial along a line and draw chainage ticks, to read pier and span stations by eye.
Run in the venv (pillow, pyproj):  python aerial-strip.py <site folder under reference/> lat0 lon0 lat1 lon1 chainage_from chainage_to half_width_m out.jpg [zoom]
Run it from the reference/ folder. Chainage is metres from lat0,lon0 along the line; zoom 1.5 gives 7.5 px per metre. The top of the strip is the left of travel.
Caveat: the orthophoto is rectified to the ground, so anything tall (arch ribs, truss tops) is displaced sideways; read stations along the line, not widths of tall things."""
import sys,json,math
from PIL import Image,ImageDraw
from pyproj import Transformer
Image.MAX_IMAGE_PIXELS=None
site=sys.argv[1]; la0,lo0,la1,lo1,c0,c1,hw=map(float,sys.argv[2:9]); out=sys.argv[9]
zoom=float(sys.argv[10]) if len(sys.argv)>10 else 1.0
j=json.load(open(f"{site}/aerial/ortho-2019.json")); im=Image.open(f"{site}/aerial/ortho-2019.jpg").convert("RGB")
t=Transformer.from_crs(4326,3776,always_xy=True); px=j["pixel_m"]
x0,y0=t.transform(lo0,la0); x1,y1=t.transform(lo1,la1); L=math.hypot(x1-x0,y1-y0); ux,uy=(x1-x0)/L,(y1-y0)/L; vx,vy=-uy,ux  # v is left of travel
def pix(x,y): return ((x-j["xmin"])/px,(j["ymax"]-y)/px)
W=int((c1-c0)/(px/zoom)); H=int(2*hw/(px/zoom))
res=px/zoom
# output pixel (a,b) -> chainage s=c0+a*res ; lateral w=hw-b*res (left positive)
o=pix(x0+ux*c0+vx*hw, y0+uy*c0+vy*hw)
# input pixel step per output a: along +u ; per output b: along -v. Image y axis is flipped (north up = smaller row)
A=( ux*res/px, uy*res/px*-1 )   # d(col,row)/da  (row = -y/px)
B=( -vx*res/px, vy*res/px )     # d(col,row)/db
im2=im.transform((W,H),Image.AFFINE,(A[0],B[0],o[0],A[1],B[1],o[1]),resample=Image.BICUBIC)
d=ImageDraw.Draw(im2)
for s in range(int(math.ceil(c0/10)*10),int(c1)+1,10):
    a=(s-c0)/res; big=(s%50==0)
    d.line((a,0,a,H if big else 14),fill=(255,255,0) if big else (255,255,255),width=1)
    if big: d.text((a+3,2),str(s),fill=(255,255,0))
d.line((0,H/2,W,H/2),fill=(0,255,255),width=1)
im2.save(out,quality=90); print(im2.size,"chainage",c0,c1,"res",res,"len",round(L,1))

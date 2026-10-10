var _____WB$wombat$assign$function_____ = function(name) {return (self._wb_wombat && self._wb_wombat.local_init && self._wb_wombat.local_init(name)) || self[name]; };
if (!self.__WB_pmw) { self.__WB_pmw = function(obj) { this.__WB_source = obj; return this; } }
{
  let window = _____WB$wombat$assign$function_____("window");
  let self = _____WB$wombat$assign$function_____("self");
  let document = _____WB$wombat$assign$function_____("document");
  let location = _____WB$wombat$assign$function_____("location");
  let top = _____WB$wombat$assign$function_____("top");
  let parent = _____WB$wombat$assign$function_____("parent");
  let frames = _____WB$wombat$assign$function_____("frames");
  let opener = _____WB$wombat$assign$function_____("opener");

function SetupContact(website_description, counter)
{
	if (counter == 1)
	{
		document.write("<a href=\"mailto:info@heritagecommunityfdn.org?Subject="+website_description+" Web Site\" title=\"Contact us by Email\">Contact us by Email</a>");
	}
	else if (counter == 2)
	{
		document.write("<a href=\"mailto:cmpsoc@telus.net?Subject="+website_description+" Web Site\" title=\"Contact MilArm by Email\">Contact MilArm by Email</a>");
	}
}

//function that swaps pictures
function Switch(imgName,imgObjName) 
{
  if (document.images) 
  {
   document.images[imgName].src = eval(imgObjName + ".src");
  }
}

//Function to open new windows
function openWin(URL, Width, Height)
{

aWindow=window.open(URL,"PopUp","width="+Width+",height="+Height+",resizable=yes,scrollbars=yes,left=100,top=60");
    
    aWindow.resizeTo(Width, Height);
    
    aWindow.focus();
    if(aWindow.opener == null)
    {
        aWindow.opener = window;
        aWindow.opener.name = "opener";
    }
}

//Function to pop up windows for images.
function Imgpop(level,szImgSource,szDescription,nCopyrightNum,szTitle)
{
	popSource = szImgSource;
    popDescription = szDescription;
    popCopyright = nCopyrightNum;
	popTitle=szTitle;
	popUrl = "";
	popCopyString ='';
	popCopyString= getCopyright(popCopyright);
	popSrc='../images/gallery/myimg.gif';
    if (popDescription == "description")
        popDescription = "";
	if (popTitle == "title")
        popTitle = 'My Images';

	width=650;
    height=750;

    //If resolution is 640x480
    if(screen.width < 800)
        height=350;
    //If resolution is 800x600
    else if(screen.width < 1024)
        height=500;

    for(i=1; i<=level; i++)
	{
		popUrl = popUrl + "../";
	}
	popUrl = popUrl + "inc/popup.html";
	openWin(popUrl,width,height);
}
//function to get copyright string
function getCopyright(popCopyright){
	
    var popCopy ='';
	switch(popCopyright){
	case 0:
		popCopy='Image &copy; Copyright The Heritage Community Foundation.';
		break;
	case 1:
		popCopy='Image &copy; Copyright Allan and Sharon Kerr,<br />Canadian Militaria Preservation Society.';
		break;
	case 2:
		popCopy='Image &copy; Copyright City of Edmonton Archives.';
		break;
	case 3:
		popCopy='Image &copy; Copyright Galt Museum.';
		break;
	case 4:
		popCopy='Image &copy; Copyright Allan and Sharon Kerr,<br />Canadian Militaria Preservation Society.';
		break;
	case 5:
		popCopy='Image &copy; Copyright Library and Archives Canada.';
		break;
	case 6:
		popCopy='Image &copy; Copyright Provincial Archives of Alberta.';
		break;		
	case 7:
		popCopy='Image &copy; Copyright Royal Alberta Museum.';
		break;		
	case 8:
		popCopy='Image &copy; Copyright Housez Studios.';
		break;		
	case 9:
		popCopy='Image &copy; Copyright Beulah Williams.';
		break;		
	case 10:
		popCopy='Image &copy; Copyright Red Deer and District Museum.';
		break;		
	default:
		popCopy='Image &copy; Copyright The Heritage Community Foundation.';
		break;
	}	
	return popCopy;
	
}
//Function to pop up windows for footnotes.
function openFootnote(level,szDescription)
{
    popDescription = szDescription;
 
    if (popDescription == "description")
        popDescription = "";
    
    width=400;
    height=150;

    if(level==0)
        openWin("footnote.html",width,height);
    
    else if(level==1)
        openWin("../footnote.html",width,height);

    else if(level==2)
        openWin("../../footnote.html",width,height);
}

// The following code uses the AJAX technology to update the SubCategories 
var xmlHttp

function showSubCategory(category_id)
{ 
	xmlHttp=GetXmlHttpObject()
	if (xmlHttp==null)
	{
		alert ("Browser does not support HTTP Request")
		return
	}
	var url="../administration/getsubcategory.php"
	url=url+"?category_id="+category_id
	url=url+"&amp;sid="+Math.random()
	xmlHttp.onreadystatechange=stateChanged 
	xmlHttp.open("GET",url,true)
	xmlHttp.send(null)
}
function stateChanged() 
{ 
	if (xmlHttp.readyState==4 || xmlHttp.readyState=="complete")
	{ 
		document.getElementById("txtsubcategory").innerHTML=xmlHttp.responseText 
	} 
}
function GetXmlHttpObject()
{
	var xmlHttp=null;
	try
	{
		// Firefox, Opera 8.0+, Safari
		xmlHttp=new XMLHttpRequest();
	}
	catch (e)
	{
		//Internet Explorer
		try
		{
			xmlHttp=new ActiveXObject("Msxml2.XMLHTTP");
		}
		catch (e)
		{
			xmlHttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
	}
	return xmlHttp;
}

 }

/*
     FILE ARCHIVED ON 16:03:33 Dec 08, 2010 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 23:00:55 Oct 10, 2026.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/

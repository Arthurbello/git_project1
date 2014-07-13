/**
 * Created by ayomidebell on 7/11/14.
 */
dynamic_display.js
function ModifyBGColor(id, newColor)
{
 var mElement = document.getElementById(id);
 mElement.style.backgroundColor = newColor;
}
function ModifyTextColor(id, newColor)
{
 var mElement = document.getElementById(id);
 mElement.style.color = newColor;
}
function ModifyBoxSize(id, newWidth, newHeight)
{
 var mElement = document.getElementById(id);
 mElement.style.width = newWidth;
 mElement.style.height = newheight;
}
function ModifyBoxPosition(id, newLeft, newTop)
{
 var mElement = document.getElementById(id);
 mElement.style.left = newLeft;
 mElement.style.top = newTop;
}
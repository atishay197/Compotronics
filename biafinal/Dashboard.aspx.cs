using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class Dashboard : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {

    }
    protected void RadioButtonList1_SelectedIndexChanged(object sender, EventArgs e)
    {
        if (RadioButtonList1.SelectedItem.Text == "Thickness")
        {
             Image2.ImageUrl = "ThicknessC.PNG";
              Image3.ImageUrl = "ThicknessTrend.PNG"; 
        }
        else if (RadioButtonList1.SelectedItem.Text == "Resolution")
        {
            Image2.ImageUrl = "ResolutionC.PNG";
            Image3.ImageUrl = "RelolutionTrend.PNG";
        }
        else if (RadioButtonList1.SelectedItem.Text == "RAM")
        {
            Image2.ImageUrl = "RAMC.PNG";
            Image3.ImageUrl = "RamTrend.PNG";
        }
        else if (RadioButtonList1.SelectedItem.Text == "Camera")
        {
            Image2.ImageUrl = "CameraC.PNG";
            Image3.ImageUrl = "CameraTrend.PNG";
        }
        else if (RadioButtonList1.SelectedItem.Text == "Internal Memory")
        {
            Image2.ImageUrl = "InternalMemoryC.PNG";
            Image3.ImageUrl = "InternalMemoryTrend.PNG";
        }
        else if (RadioButtonList1.SelectedItem.Text == "Screen Size")
        {
            Image2.ImageUrl = "ScreenSizeC.PNG";
            Image3.ImageUrl = "SizeTrend.PNG";
        }
        else if (RadioButtonList1.SelectedItem.Text == "Pixel Density")
        {
            Image2.ImageUrl = "PixelDensityC.PNG";
            Image3.ImageUrl = "PixelDensityTrend.PNG";
        }
        else if (RadioButtonList1.SelectedItem.Text == "TalkTime")
        {
            Image2.ImageUrl = "TalktimeC.PNG";
            Image3.ImageUrl = "TalktimeTrend.PNG";
        }
        else if (RadioButtonList1.SelectedItem.Text == "Weight")
        {
            Image2.ImageUrl = "WeightC.PNG";
            Image3.ImageUrl = "WeightTrend.PNG";
        }
        else if (RadioButtonList1.SelectedItem.Text == "Price")
        {
            Image2.ImageUrl = "PriceC.PNG";
            Image3.ImageUrl = "PriceTrend.PNG";
        }
    }
    protected void DropDownList1_SelectedIndexChanged(object sender, EventArgs e)
    {
        if (DropDownList1.SelectedItem.Text == "2007")
            Image4.ImageUrl = "2007.png";
        else if (DropDownList1.SelectedItem.Text == "2008")
            Image4.ImageUrl = "2008.png";
        else if (DropDownList1.SelectedItem.Text == "2009")
            Image4.ImageUrl = "2009.png";
        else if (DropDownList1.SelectedItem.Text == "2010")
            Image4.ImageUrl = "2010.png";
        else if (DropDownList1.SelectedItem.Text == "2011")
            Image4.ImageUrl = "2011.png";
        else if (DropDownList1.SelectedItem.Text == "2012")
            Image4.ImageUrl = "2012.png";
        else if (DropDownList1.SelectedItem.Text == "2013")
            Image4.ImageUrl = "2013.png";
        else if (DropDownList1.SelectedItem.Text == "2014")
            Image4.ImageUrl = "2015.png";
        else if (DropDownList1.SelectedItem.Text == "2016")
            Image4.ImageUrl = "2016.png";
       
    }
    protected void DropDownList3_SelectedIndexChanged(object sender, EventArgs e)
    {
        if (DropDownList3.SelectedItem.Text == "First")
            Image4.ImageUrl = "1.png";
        else if (DropDownList3.SelectedItem.Text == "Second")
            Image4.ImageUrl = "2.png";
        else if (DropDownList3.SelectedItem.Text == "Third")
            Image4.ImageUrl = "3.png";
        else if (DropDownList3.SelectedItem.Text == "Fourth")
            Image4.ImageUrl = "4.png";
    }
    
    protected void DropDownList4_SelectedIndexChanged(object sender, EventArgs e)
    {
        if (DropDownList4.SelectedItem.Text == "RAM")
            Image5.ImageUrl = "RAMSalesTrend.PNG";
        else if (DropDownList4.SelectedItem.Text == "Size")
            Image5.ImageUrl = "SizeSaleTrend.PNG";
        else if (DropDownList4.SelectedItem.Text == "Thickness")
            Image5.ImageUrl = "ThicknessSalesTrend.PNG";
        else if (DropDownList4.SelectedItem.Text == "Total")
            Image5.ImageUrl = "TotalSales.PNG";

    }
}
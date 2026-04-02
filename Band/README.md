# Band Website

## What We Did
- Made a website for our fictional band 
- [THE FAST FOOD EATERS WEBSITE](https://lemondog39.github.io/)

- For formatting, we used the below websites for help. 
- This included getting the text and images to appear centered, adding a background gif, resizing images, and choosing the color of our header text. 
 - [HTML Cheat Sheet](https://websitesetup.org/wp-content/uploads/2019/08/HTML-CHEAT-SHEET.png)
   - This was taken from the class repository. 
   - Aside from this cheat sheet, we also referenced the html and style.css file of the given example website from the Band assignment markdown file in the class repository. 
   - [Example Website](https://kariestes.github.io/)
 - [HTML Help Website](https://www.w3schools.com/html/default.asp) 
 
## How We Did It (and what went wrong)
- We started by referencing the example website on how to structure our website in terms of the html code. 
- At first, the images weren't showing up, and all the text was aligned to the left. Our mp3 file was also not playing. 
- We figured out it was because although all the png and mp3 files were in my folder, I had forgotten to upload everything to the actual repository, so there were no png or mp3 files for the html file to reference from. 

- To fix the formatting, we also referenced the example website's css file. At first it didn't work for the exact same reason as the images (I had forgotten to upload it to the repository), but after we did that the website was formatted the way we wanted (with text and images aligned to the center). 

- After we uploaded the style.css file, it looked fine except for the fact that the text would go off the website page. 
- We tried to fix this by referencing the [HTML Help Website](https://www.w3schools.com/html/default.asp), which stated that we could try using <b></b> for paragraph breaks? 
- This actually did not work but instead would bold whatever text was within the <b></b> command. 
- When we took it out, the text stopped going off the screen and was perfectly aligned as centralised paragraphs? 
- Magic i guess. I think it was the CSS file that finally worked (maybe we should've waited a bit longer for the website to update lol). 

- We were done with the website but thought it would be cool and funny to have a gif as a background. We didn't know how to do that so we tried editing the CSS file with this line of code from the [HTML Help Website](https://www.w3schools.com/html/default.asp)

`
body {
  background-image: url('img_girl.jpg');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: 100% 100%;
}
`

- This did not work so we had to do inline CSS coding and instead plonk it directly into the html index file, and for the CSS file we had the background just be white color. 

## Assessment 
### Of myself
- I hosted the website with my github.io website that I published to the internet last week. 
- I was also mainly in charge of coding the website as it was all done on my laptop. 

### Of teammates
- Leo helped a lot with the troubleshooting and testing of the website to make sure that everything was looking the way we wanted it to and running correctly, and also pointed out any anomalies and errors so that we could fix it. 
- Zetong did all the images, the background gif and found the mp3 file and airdropped them to me. He also wrote the description of the band. 
- All three of us contributed in deciding how to format the website (as in we kind of discussed and like looked at it each time we wrote in something new and suggested changes), and we each wrote our own bios. 

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links a![Figure_1](https://user-images.githubusercontent.com/97498951/211147586-8bb7a7e3-88b6-477a-835e-0df8c9e8b3b6.png)
re enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

  <h3

## <p> Web Scraping on E-commerce Sites</p>

<!-- PROJECT LOGO -->

<div align="left">
  <a href="">
    <img src="https://miro.medium.com/max/1400/1*1QcqrOoDE1rKa0NTp1iEtw.png" alt="Logo" width="500" height="250">
  </a>
  </div>
  
  
  <br />
  <p align="left">
   This simple project attempts to scape product listings data from e-commerce sites and visualise them using Tableau.
    <br />
   
  </p>




![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
<!-- ABOUT THE PROJECT -->
## About The Project
                         
<div align="">
  <a href="">
    <img src="https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1587503051/web1_jpfixv.png" alt="Logo" width="500" height="250">
  </a>

<br />
  <br />
<p align="justify">Web Scraping is the process of collecting information from a particular website by downloading the html contents of the site and then parsing that data to extract the data of interest. Some of the main use cases of web scraping include information gathering, market research and etc. Web scraping is used by individuals or businesseses who want to make use of publicly available web data to make smarter decisions.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)


## Built With
<div align="">
  <a href="">
    <img src="https://www.devopsschool.com/blog/wp-content/uploads/2022/03/Python-01-2.png" alt="Logo" width="100" height="60">
     <img src="https://crackerzin.com/wp-content/uploads/2020/05/tableau.png" alt="Logo" width="100" height="60">
    <img src="https://blog.knoldus.com/wp-content/uploads/2021/03/selenium.png" alt="Logo" width="100" height="60">
  </a>
  


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
## Process Flow 
### Web Scraping

![image](https://user-images.githubusercontent.com/97498951/216298637-bcb187f8-96ad-48f1-8fbe-768857552f5e.png)

   1. Import selenium, pandas, time, and the re modules
   2. Define the path of the chromedriver.exe
   3. Open Chrome(or other browsers) using the webdriver imported from Selenium.
   4. Proceed to the webpage ''https://www.lazada.com.my/shop-mobiles/apple/'
   5. Find the xpath of the title and price of each listing. Also, find the xpath of the "next page" button.
   6. Loop the web scraping process based on the total number of pages displayed on the website.
   7. Convert the newly created list with all the listing's title and pricing details into a DataFrame using pandas.
   8. Define a function to remove emojis from the listing's title and apply it in the DataFrame.
   9. Export the DataFrame into csv.
  
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## [Tableau Dashboard](https://public.tableau.com/app/profile/zhiming/viz/IphoneListingsonLazadaDashboard/Dashboard1?publish=yes)

![image](https://user-images.githubusercontent.com/97498951/216310882-0122d036-5907-4866-a6c6-80eb2af52229.png)

[ Click Here To View The Dashboard ](https://public.tableau.com/app/profile/zhiming/viz/IphoneListingsonLazadaDashboard/Dashboard1?publish=yes)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Findings
- There are a total 124 Apple smartphone's listings on Lazada
- Iphone 14 has the most number of listings (35 units)
- The cheapest listed apple phone is "Iphone 5S - 16GB (Demo)" and the most expensive apple smartphone listed is "Apple Iphone 13 Pro Max 1 TB"
- The median price for Iphone 14 regardless of price and storage space is RM 4,699. The cheapest price for this model is RM 3,899 and the highest price is RM 5,799.
- The median price for Iphone 13 regardless of price and storage space is RM 3,899. The lowest price listed for Iphone 13 is RM 3,199 and the most expensive phone is listed for RM 7,269.
- There are only one iPhone XS and one iPhone 5S listed on Lazada.
- There are two listings of Apple Iphone 12 which are located outside the whisker of the boxplot. This indicates that these 2 listings are outliers and they are highly likely to have the wrong pricing.






![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
<!-- References -->
## References 
* [Text Cleaning (Remove Emojis) ](https://gist.github.com/slowkow/7a7f61f495e3dbb7e3d767f97bd7304b)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Python]: https://1000logos.net/wp-content/uploads/2020/08/Python-Logo.jpg


# Home Sales Analysis

### Project Overview
The purpose of this project is to create a model that helps Home sellers(real estate agent, 
developers and investors) on features that influence the average price of a house in king county, Washington.
### Data Overview
We analyzed dataset which contains infomation about different houses between 2014 and 2015.
The objective was to build a model and predict the sale price using the given features and comparing their relationships between them and price.


The data schema is as follows:

The columns of the data: 
* `id` - Unique identifier for a house
* `date` - Date house was sold
* `price` - Sale price (prediction target)
* `bedrooms` - Number of bedrooms
* `bathrooms` - Number of bathrooms
* `sqft_living` - Square footage of living space in the home
* `sqft_lot` - Square footage of the lot
* `floors` - Number of floors (levels) in house
* `waterfront` - Whether the house is on a waterfront
  * Includes Duwamish, Elliott Bay, Puget Sound, Lake Union, Ship Canal, Lake Washington, Lake Sammamish, other lake, and river/slough waterfronts
* `view` - Quality of view from house
  * Includes views of Mt. Rainier, Olympics, Cascades, Territorial, Seattle Skyline, Puget Sound, Lake Washington, Lake Sammamish, small lake / river / creek, and other
* `condition` - How good the overall condition of the house is. Related to maintenance of house.
    * 1 = Poor- Worn out. Repair and overhaul needed on painted surfaces, roofing, plumbing, heating and numerous functional inadequacies. Excessive deferred maintenance and abuse, limited value-in-use, approaching abandonment or major reconstruction 
    * 2 = Fair- Badly worn. Much repair needed. Many items need refinishing or overhauling, deferred maintenance obvious, inadequate building utility and systems all shortening the life expectancy and increasing the effective age.
    * 3 = Average- Some evidence of deferred maintenance and normal obsolescence with age in that a few minor repairs are needed, along with some refinishing. All major components still functional and contributing toward an extended life expectancy. Effective age and utility is standard for like properties of its class and usage.
    * 4 = Good- No obvious maintenance required but neither is everything new. Appearance and utility are above the standard and the overall effective age will be lower than the typical property.
    * 5= Very Good- All items well maintained, many having been overhauled and repaired as they have shown signs of wear, increasing the life expectancy and lowering the effective age with little deterioration or obsolescence evident with a high degree of utility.
* `grade` - Overall grade of the house. Related to the construction and design of the house.
    * Represents the construction quality of improvements. Grades run from grade 1 to 13. Generally defined as:
        * 1-3 Falls short of minimum building standards. Normally cabin or inferior structure.
        * 4 Generally older, low quality construction. Does not meet code.
        * 5 Low construction costs and workmanship. Small, simple design.
        * 6 Lowest grade currently meeting building code. Low quality materials and simple designs.
        * 7 Average grade of construction and design. Commonly seen in plats and older sub-divisions.
        * 8 Just above average in construction and design. Usually better materials in both the exterior and interior finish work.
        * 9 Better architectural design with extra interior and exterior design and quality.
        * 10 Homes of this quality generally have high quality features. Finish work is better and more design quality is seen in the floor plans. Generally have a larger square footage.
        * 11 Custom design and higher quality finish work with added amenities of solid woods, bathroom fixtures and more luxurious options.
        * 12 Custom design and excellent builders. All materials are of the highest quality and all conveniences are present.
        * 13 Generally custom designed and built. Mansion level. Large amount of highest quality cabinet work, wood trim, marble, entry ways etc.
* `sqft_above` - Square footage of house apart from basement
* `sqft_basement` - Square footage of the basement
* `yr_built` - Year when house was built
* `yr_renovated` - Year when house was renovated
* `zipcode` - ZIP Code used by the United States Postal Service
* `lat` - Latitude coordinate
* `long` - Longitude coordinate
* `sqft_living15` - The square footage of interior housing living space for the nearest 15 neighbors
* `sqft_lot15` - The square footage of the land lots of the nearest 15 neighbors

### Methodology

* Data Analysis: After understanding the problem we wanted to solve, we cleaned and analyze the data, dropping feature we deemed not important in terms of the problem.
* Feature Engineering: An indepth analysis of each colums and how they relate to solving the problem.
* Feature selection: Looking for relationships between the features and how they affect the price. 
* Model Building: Building different models of different features and how they can learn the data and be able to predict them.

### Project Results

We built a multivariate regression model which combines all the features into a single model. Then, built a model for each feature and adding more complexity. The results produced three features that the home sellers can control:
* grade
* bathroom
* square foot of living

These features yield a high Rsquared score of 54%. 

### Next Steps

* Cannot use the model for other location based on the location the data is pulled from. 
*  Would like to include macro and micro features that could have an effect on the house prices. 
* Example to consider includes Economic indicators, crime rate, properties sold in other counties, mortgage rates and reports on enviromental quality.

### Repository Navigation
* Data
* Notebook
* King_County_home_price_notebook
* Presentation
* README

### AUthors

* Crystal Gould Perrott
* Titilayo Amuwo
* Michael Ajayi

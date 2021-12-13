# HP-Support-Community-Bot

Python bot which uses the WebDriver API/Selenium to operate on the HP Support Community and automatically handle certain requests, effectively improving productivity on the user forum. Bot is capable of properly handling exceptions and will notify the requester if any information was inaccessible or inputs were invalid.

Logs into a Microsoft Azure MySQL database to cache requests and retrieve information in case the request is made again. Tested on an Amazon EC2 instance.

(Fully operational but no longer in service)

## Usage

In any forum thread on the HP Support Community, mention the bot's username `@EddyK_Bot`, followed by any of the following flags and then the relevant argument. Flags and their relevant arguments are separated by commas.

| Full Flag Name  | Flag Abbreviation(s) | Argument Type | Description |
| ------------- | ------------- | - | - |
| Product: (Required flag) | Name \| P | The full, proper HP product name/number/SN - shortened identifier will work | Required to identify the product requested |
| Specifications:  | Specs \| S | Component name | Requests specifications of the product - add keywords to specify certain components or leave empty for the full specifications list |
| Maintenance: | Main \| M | Page number | Requests the Maintenance and Service guide for the product - add a page number to specify the default page when opening the PDF |
| Drivers: | Software \| D | HP SoftPaq number | Requests drivers and their relevant information such as fixes or version name |
| Support: | N/A | N/A | Provides support options that are specific to the original poster's country of residence |

## Example

### Request:
<p align="center"><img src="https://user-images.githubusercontent.com/39893918/145757860-21e85ab2-4a46-42d3-85bb-f805da53871f.jpeg" width="800"/></p>

Here, the request is for the laptop HP Spectre x360 - 13-ap0101ng, which can be shortened to just the identifier - ap0101ng - as well as the specifications with only specific categories, the microprocessor, memory, hard (drive) and display. The Maintenance and Service Guide was also specified and there was a request for 3 different SoftPaqs.

### Answer:
Below, you can find a screenshot of the bot's answer to the request:
<p align="center"><img src="https://user-images.githubusercontent.com/39893918/145758859-01d5d5ff-c409-4ffe-bc6d-d34a2b478da0.jpeg" width="800"/></p>

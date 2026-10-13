# Programmatically pulling cold-related deaths in Cook County

This is built off of [a bot we built to track heat-related deaths](https://github.com/cam-rodriguez/cpm_heatbot) 

The newest data is available in [`today_colddeaths.csv`](data/today_colddeaths.csv). A daily archive of cold deaths is in [`./data/archive`](data/archive).

## What's available

The Cook County Medical Examiner's Office makes [a digital case archive](https://datacatalog.cookcountyil.gov/Health-Human-Services/Medical-Examiner-Case-Archive/cjeq-bs86/about_data) available on the Cook County Data Portal. That archive has all deaths within the county that fall under the Medical Examiner's jurisdiction. It also includes a flag, `cold_related`, that indicates whether a death is related to cold or environmental exposure.

## How it works

`script.sh` runs the whole thing, which is triggered hourly by a cron job in Github Actions. Upon each deployment, `pull.py` runs and:
* Accesses the dataset
* Queries the data based on SoQL
* Downloads a copy of the raw data, as well as an archived version of that day's data
* Checks if there is any change between the last slice of data and the newest one
* Sends a Slack message to a designated channel within the newsroom's workspace that gives an update, with the current number of cold-related deaths.
* Cleans and processes the data for future analysis and visualizations

This was the heat-related death message from [cpm_heatbot](https://github.com/cam-rodriguez/cpm_heatbot):
![a photo of the slack message that gets sent with every deployment](./scratch/messageexample.png)

### Caveats
It isn't perfect, and this is primarily a measure to ensure that we don't have to check the data every day, as well as that we don't miss a new cold-related death added by the Medical Examiner in the portal.

Deaths are often added retroactively, so a new row doesn't inherently equal the most recent death. It's just the most recently-added death.

## How to run your own version
* Fork the repo
* Obtain an app token from the Cook County data portal in order to avoid rate-limiting from Socrata
* Set up a Slack app, create a channel to send messages to, then generate an incoming webhook url
* Set the app token and Slack webhook url as secrets within the repo
* Frequency of the job is set in the Actions `check.yml` file. Tweak as necessary.

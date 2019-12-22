# Scientific Data Analysis 2019/2020

The following instructions describe how to generate the data required for running the experiments conducted during this project.

## Specifications
All experiments were run on the Linux operating system, using Ubuntu 16.04 up to Ubuntu 19.10. Experiments require at least Python 3, preferably Python 3.7 or higher.

## Setting up
Our experiments rely on data files of Gigabytes in size. Since Canvas can not handle files of these sizes, we are forced to store our source data on external services.
Our data generating file, `data_generator.py`, relies on Python 3.7.5. It can be run as follows: `python3 data_generator.py`.
Besides creating the necessary data, this file will also look for any missing modules on the user's system and list these. These modules must be installed manually using `pip3 install`.

## Experiments
Experiments can be run by navigating to the `experiments` folder and running Python scripts from here. The results are both stored as `.png` images in the `results` folder, as well as shown as an interactive figure.

### Descriptions
- `amount_stops_vs_delays_per_day.py`: Experiment description
- `canceled_per_delay.py`: Generate a scatter plot of the number of delayed stops versus the number of canceled trains
- `correlation_trackdelays.py`: Experiment description
- `delay_11pm_histogram.py`: Plot to find the delay distribution at 11:00 pm
- `delay_1pm_histogram.py`: Plot to find the delay distribution at 1:00 pm
- `delay_5pm_histogram.py`: Plot to find the delay distribution at 5:00 pm
- `delay_8am_histogram.py`: Plot to find the delay distribution at 8:00 am
- `delay_distribution.py`: Experiment description
- `delay_histogram.py`: Experiment description
- `delay_histogram2.py`: Experiment description
- `delay_histogram_log.py`: Experiment where log values are taken to prove that the overal delay (in minutes) follows a lognormal distribution (incl. ks test).
- `delay_time_distribution.py`: Fit the exponential distribution over the frequency of _x_ minutes delay
- `delayed_per_total.py`: Show amount of delayed stops versus the total number of stops for every company in the data set.
- `delayed_train_station_percentage.py`: Experiment description
- `hourly.py`: Experiment description
- `normalize_wind_delay.py`: Plot to find the relation between the windspeed in the Netherlands and the number of delayed trains, both on a single day and normalized.
- `normalized_rain_delay.py`: Plot to find the relation between the rain in the Netherlands and the number of delayed trains, both on a single day and normalized.
- `overtime.py`: Experiment description
- `overtime_montues_diffs.py`: Experiment description
- `overtime_weekday.py`: Experiment description
- `overtime_weekday_filtered.py`: Experiment on amount of delayed stops per weekday, with a ks test for normal distribution.
- `overtime_weekend.py`: Experiment description
- `overtime_weekend_diffs.py`: Experiment descriptionx
- `station.py`: Experiment description
- `station_relative.py`: Experiment description
- `station_relative_5.py`: Experiment description
- `train_type_delays.py`: Show a bar plot with the amount of delays for every carrier type of the NS
- `weather_delay_rain.py`: Plot to find the relation between the rain in the Netherlands and the minutes of delay of all trains, both on a single day.
- `weather_delay_wind.py`: Plot to find the relation between the windspeed in the Netherlands and the minutes of delay of all trains, both on a single day.
- `weather_delayornot_rain.py`: Experiment description
- `weather_delayornot_rain_percentage.py`: Plot to find the relation between the rain in the Netherlands and the number of delayed trains (percentage), both on a single day.
- `weather_delayornot_wind.py`: Plot to find the relation between the rain in the Netherlands and the number of delayed trains, both on a single day.
- `weather_delayornot_wind_percentage.py`: Plot to find the relation between the rain in the Netherlands and the number of delayed trains (percentage), both on a single day.
- `weekday.py`: plot showing amount of stops and delays per weekday (total)
- `weekdays.py`: Experiment description

## Contributors
Daan Vinken, Joël Buter, Ricardo van Aken, Jesse Postema

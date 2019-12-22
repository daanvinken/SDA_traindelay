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
- `weather_delay_rain.py`: Experiment description
- `weekday.py`: Experiment description
- `overtime.py`: Experiment description
- `normalize_wind_delay.py`: Experiment description
- `train_type_delays.py`: Experiment description
- `delay_8am_histogram.py`: Experiment description
- `delay_histogram2.py`: Experiment description
- `overtime_weekday_filtered.py`: Experiment description
- `weather_delay_wind.py`: Experiment description
- `normalized_rain_delay.py`: Experiment description
- `amount_stops_vs_delays_per_day.py`: Experiment description
- `weather_delayornot_rain_percentage.py`: Experiment description
- `delay_histogram_log.py`: Experiment description
- `delayed_per_total.py`: Experiment description
- `weather_delayornot_wind.py`: Experiment description
- `weekdays.py`: Experiment description
- `delay_11pm_histogram.py`: Experiment description
- `overtime_weekend.py`: Experiment description
- `weather_delayornot_wind_percentage.py`: Experiment description
- `station.py`: Experiment description
- `delay_time_distribution.py`: Experiment description
- `station_relative.py`: Experiment description
- `correlation_trackdelays.py`: Experiment description
- `delay_1pm_histogram.py`: Experiment description
- `hourly.py`: Experiment description
- `get_files.py`: Experiment description
- `station_relative_5.py`: Experiment description
- `overtime_weekday.py`: Experiment description
- `delay_5pm_histogram.py`: Experiment description
- `weather_delayornot_rain.py`: Experiment description
- `canceled_per_delay.py`: Experiment description
- `delay_distribution.py`: Experiment description
- `delayed_train_station_percentage.py`: Experiment description
- `delay_histogram.py`: Experiment description
- `overtime_montues_diffs.py`: Experiment description
- `overtime_weekend_diffs.py`: Experiment description

## Contributors
Daan Vinken
Joël Buter
Ricardo van Aken
Jesse Postema

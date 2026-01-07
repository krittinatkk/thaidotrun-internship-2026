# Data Dictionary: bkk_data_final.csv

## Overview
Dataset containing running event registration data from ThaiDotRun platform.

## Columns

| Column | Type | Description | Sample Values |
|--------|------|-------------|---------------|
| ID | string | Unique registration ID | `42dd3888764e5aaeaffdb122c5e838d8abaa79136952e09e0df605bd91745185` |
| registrationId | string | Registration transaction ID | `65920b63dac26d73d186a6c7` |
| gender | string | Participant gender | `female`, `male` |
| birthDate | string | Date of birth (YYYY-MM-DD) | `1987-02-12` |
| eventName | string | Name of running event | `RECYCLE for LIFE "WE CAN RUN FUND FOR LEGS"` |
| isVirtual | boolean | Virtual event flag | `false`, `true` |
| ticketTypeName | string | Type of ticket purchased | `Early bird : Mini Marathon 10 KM` |
| ticketTypePrice | integer | Ticket price in THB | `600` |
| province | string | Province of registrant | `Bangkok` |
| registerDate | string | Registration date (YYYY/MM/DD) | `2024/01/01` |
| shirtType | string | Type of event shirt | `Short Sleeves (10 KM)` |
| shirtSize | string | Shirt size with measurements | `S : chest 36"` |
| country | string | Country | `Thailand` |
| city | string | City | `Ratburana` |
| postalCode | string | Postal code | `10140` |

## Initial Observations
1. Most registrations are from Bangkok
2. Mix of virtual and physical events
3. Prices range from 0 to 2543 THB
4. Some columns have missing values (city, postalCode, country)

## Next Steps
1. Calculate age from birthDate
2. Extract distance from ticketTypeName
3. Handle missing values
4. Analyze event popularity

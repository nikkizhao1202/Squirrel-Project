# Squirrel Tracker Project

<ul>
  <li> Group Name: Project Group 85 </li>
  <li> Tools For Analytics (Section: 2) </li>
  <li> Contributors: Yongyi(Nikki)Zhao, Jieming Bian</li>
  <li> UNI: yz3706 ; jb4382 </li>
</ul>

## Overview
<p> Squirrel Tracker is a web application project which provides the users with the visualized sightings of squirrels on the map around Central Park at Manhattan, NYC. Specifically, it can import squirrel data and alls end users to add, update and edit data. 
</p>

## Details
<ul>
  <li> Management Commands </li>
    <p> Import: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command. 

  ```sh
  python manage.py import_squirrel_data /path/to/file.csv
  ```

  Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line          
  after the name of the management command.

   ```sh
  python manage.py export_squirrel_data /path/to/file.csv
   ```
   </p>
  <li> Views </li>
    <p>
    
  1. A view that shows a map that displays the location of the squirrel sightings on an OpenStreets map

         Located at: /map

         Method: GET


  2. A view that lists all squirrel sightings with links to edit and add sightings

         Located at: /sightings

         Method: GET

  3. A view to update a particular sighting

          Located at: /sightings/
        
          Method: POST

  4. A view to create a new sighting

          Located at: /sightings/add

          Method: POST

  5. A view to delete a sighting

          Located at: /sightings/
        
          Method: DELETE

  6. A view with general statistics about the sightings

          Located at: /sightings/stats
        
         Method: GET
 </p>
</ul>

## Data Source
We use squirrel data [**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) which was counted by the [**Squirrel Census**](https://www.thesquirrelcensus.com/). 

## Requirements
<ul>
  <li> Python (3.6, 3.7) </li>
  <li> Django (2.2) </li>
</ul>

## Reference Matrial
<ul>
  <li>https://docs.djangoproject.com/en/3.0/intro/tutorial01/</li>
  <li>https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/</li>
</ul>

## Discussion and Development

<p> Most development discussion is taking place on github in this repo.</p>

## Contributing to Squirrel Tracker
<p>
This is a semester project dedicated for IEOR 4501 Tools for Analytics. Any contributions, bug reports, bug fixes, documentation improvements, enhancements to make this project better are warmly welcomed.
</p>

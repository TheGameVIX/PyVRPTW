Shared Dependencies:

1. Libraries: PyQt, PyVRP, pandas, folium, nominatim, OSRM, openpyxl, logging.

2. Data Schemas: 
   - Input data schema: Address, City, State, Zip Code, Number of Techs, Number of Time Windows, Time Windows, Max Jobs Per day Per Tech, Average Job Duration, Break Time per tech, Days of the week the techs can visit the sites.
   - Output data schema: Tech, Week, Address, State, Zip Code, TimeSlot, Day.

3. Variables:
   - User input variables: num_techs, num_time_windows, time_windows, max_jobs_per_day_per_tech, avg_job_duration, break_time_per_tech, days_of_week.
   - Geocoding variables: geocoded_cache, failed_to_geocode.
   - VRP variables: distance_matrix, clusters, depot.
   - Output variables: optimized_schedule, map.

4. File Names: 
   - Input file: user uploaded .xlsx file.
   - Output files: geocoded_cache.csv, failed_to_geocode.csv, optimized_schedule.xlsx, log.txt.

5. Function Names:
   - UI functions: upload_file, confirm_upload, enter_button_clicked, show_progress, show_optimization_complete.
   - Geocoding functions: geocode_address, cache_geocodes, handle_failed_geocodes.
   - VRP functions: create_clusters, calculate_distance_matrix, solve_vrp, generate_map.
   - Output functions: write_schedule, log_errors.

6. DOM Elements:
   - PyQt UI elements: upload_button, confirmation_message, enter_button, progress_bar, optimization_complete_window.

7. Message Names:
   - Confirmation message: "File has been uploaded."
   - Progress bar messages: "Optimization phase: [current phase]"
   - Completion message: "Optimization complete."
   - Error messages: logged in log.txt.
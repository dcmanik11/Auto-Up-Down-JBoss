import pygetwindow as gw

# Get all windows
windows = gw.getAllTitles()

# Filter windows with the first name "Administrator"
filtered_windows = [window for window in windows] # if window.startswith('')

# Print the filtered windows
for window in filtered_windows:
    print(window)
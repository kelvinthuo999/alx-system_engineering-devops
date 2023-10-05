#!/bin/bash

# Check if the script is run with root (sudo) privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script with sudo or as root."
  exit 1
fi

# Define the new IP address mappings
new_hosts_entries=(
  "127.0.0.3 localhost"
  "8.8.8.8 facebook.com"
)

# Create a temporary hosts file
temp_hosts_file=$(mktemp)

# Copy the original /etc/hosts file to the temporary file
cp /etc/hosts "$temp_hosts_file"

# Loop through the new host entries and modify the temporary file
for entry in "${new_hosts_entries[@]}"; do
  sed -i "s/^.*$(echo $entry | cut -d' ' -f2).*\$/$entry/" "$temp_hosts_file"
done

# Replace the original /etc/hosts file with the modified version
cp -f "$temp_hosts_file" /etc/hosts

# Clean up the temporary file
rm -f "$temp_hosts_file"

echo "Hosts file has been updated."


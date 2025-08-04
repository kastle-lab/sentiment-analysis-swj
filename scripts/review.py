import pandas as pd
import os
import sys
from pathlib import Path

def find_next_unprocessed_row(df, start_range, end_range, analyst_name):
    """Find the next row that hasn't been processed by this analyst."""
    for i in range(start_range, end_range + 1):
        # Check if this row hasn't been processed by this analyst
        if pd.isna(df.loc[i, 'analyst']) or df.loc[i, 'analyst'] == '' or df.loc[i, 'analyst'] != analyst_name:
            return i
    return None

def main():
    # Get CSV filename
    file_name = input("Enter the CSV filename (with .csv extension): ").strip()
    csv_filename = Path(__file__).parent.parent / 'Deliverables' / 'Data' / f'{file_name}' 

    # Check if file exists
    if not os.path.exists(csv_filename):
        print(f"Error: File '{csv_filename}' not found.")
        return
    
    try:
        # Read CSV into DataFrame
        df = pd.read_csv(csv_filename)
        print(f"Successfully loaded CSV with {len(df)} rows.")
        
        # Check if required columns exist
        if 'comment' not in df.columns:
            print("Error: 'comment' column not found in CSV.")
            return
        
        # Add sentiment and analyst columns if they don't exist
        if 'sentiment' not in df.columns:
            df['sentiment'] = ''
        if 'analyst' not in df.columns:
            df['analyst'] = ''
        
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return
    
    # Get user name
    analyst_name = input("Enter your name: ").strip()
    if not analyst_name:
        print("Error: Name cannot be empty.")
        return
    
    # Get range from user
    print(f"\nTotal rows in dataset: {len(df)}")
    try:
        start_range = int(input("Enter starting row number (0-based indexing): "))
        end_range = int(input("Enter ending row number (inclusive): "))
        
        # Validate range
        if start_range < 0 or end_range >= len(df) or start_range > end_range:
            print(f"Error: Invalid range. Please enter values between 0 and {len(df)-1}.")
            return
            
    except ValueError:
        print("Error: Please enter valid numbers for the range.")
        return
    
    # Check for existing work by this analyst in this range
    existing_work = df.loc[start_range:end_range, 'analyst'] == analyst_name
    completed_count = existing_work.sum()
    
    if completed_count > 0:
        print(f"\nFound {completed_count} rows already completed by {analyst_name} in this range.")
        resume_choice = input("Do you want to resume from where you left off? (y/n): ").strip().lower()
        if resume_choice != 'y':
            print("Exiting program.")
            return
    
    # Display sentiment options
    sentiment_options = {
        1: "Extremely Negative",
        2: "Slightly Negative", 
        3: "Neutral",
        4: "Slightly Positive",
        5: "Extremely Positive"
    }
    
    print("\nSentiment Options:")
    for key, value in sentiment_options.items():
        print(f"{key}. {value}")
    print("\nCommands:")
    print("- Enter 1-5 for sentiment rating")
    print("- Type 'skip' to skip current row")
    print("- Type 'quit' to exit and save progress")
    print("- Type 'status' to see progress")
    
    # Create output filename
    base_filename = os.path.splitext(csv_filename)[0]
    output_filename = f"{base_filename}_{analyst_name.replace(' ', '-')}.csv"
    
    # Process each row in the specified range
    current_row = find_next_unprocessed_row(df, start_range, end_range, analyst_name)
    
    if current_row is None:
        print(f"\nAll rows in range {start_range}-{end_range} have already been completed by {analyst_name}!")
        print("No further work needed.")
        return
    
    total_rows = end_range - start_range + 1
    
    while current_row is not None and current_row <= end_range:
        completed_in_range = sum(1 for i in range(start_range, end_range + 1) 
                               if not pd.isna(df.loc[i, 'analyst']) and df.loc[i, 'analyst'] == analyst_name)
        remaining = total_rows - completed_in_range
        
        print(f"\n--- Row {current_row} ({completed_in_range + 1}/{total_rows}, {remaining - 1} remaining) ---")
        comment = df.loc[current_row, 'comment']
        
        # Handle missing or empty comments
        if pd.isna(comment) or str(comment).strip() == '':
            print("Comment: [EMPTY OR MISSING]")
        else:
            print(f"Comment: {comment}")
        
        # Check if this row was already processed by this analyst
        if not pd.isna(df.loc[current_row, 'analyst']) and df.loc[current_row, 'analyst'] == analyst_name:
            current_sentiment = df.loc[current_row, 'sentiment']
            print(f"Already processed by you as: {current_sentiment}")
            overwrite = input("Overwrite existing rating? (y/n): ").strip().lower()
            if overwrite != 'y':
                current_row = find_next_unprocessed_row(df, current_row + 1, end_range, analyst_name)
                continue
        
        # Get sentiment rating from user
        while True:
            try:
                choice = input("\nEnter sentiment rating (1-5), 'skip', 'quit', or 'status': ").strip().lower()
                
                if choice == 'quit':
                    print(f"\nProgress saved to '{output_filename}'.")
                    print(f"You can resume later by running the program again with the same name and range.")
                    print("Goodbye!")
                    return
                
                elif choice == 'skip':
                    print("Skipping this row.")
                    break
                
                elif choice == 'status':
                    completed_in_range = sum(1 for i in range(start_range, end_range + 1) 
                                           if not pd.isna(df.loc[i, 'analyst']) and df.loc[i, 'analyst'] == analyst_name)
                    remaining = total_rows - completed_in_range
                    print(f"Progress: {completed_in_range}/{total_rows} completed, {remaining} remaining")
                    continue
                
                choice = int(choice)
                if choice in sentiment_options:
                    # Update DataFrame with sentiment and analyst name
                    df.loc[current_row, 'sentiment'] = sentiment_options[choice]
                    df.loc[current_row, 'analyst'] = analyst_name
                    print(f"Recorded: {sentiment_options[choice]}")
                    
                    # Save after each entry
                    try:
                        df.to_csv(output_filename, index=False)
                        print(f"Progress saved to '{output_filename}'")
                    except Exception as e:
                        print(f"Warning: Could not save file: {e}")
                    
                    break
                else:
                    print("Please enter a number between 1 and 5, or use 'skip', 'quit', or 'status'.")
                    
            except ValueError:
                print("Please enter a valid number between 1 and 5, or use 'skip', 'quit', or 'status'.")
        
        # Find next unprocessed row
        current_row = find_next_unprocessed_row(df, current_row + 1, end_range, analyst_name)
    
    # Final save and completion message
    try:
        df.to_csv(output_filename, index=False)
        print(f"\nThank you, {analyst_name}! Your complete analysis has been saved to '{output_filename}'.")
        print("All rows in your specified range have been completed. Great work!")
        
    except Exception as e:
        print(f"Error saving final file: {e}")

if __name__ == "__main__":
    main()
import subprocess
import os

if __name__ == "__main__":
    # Define the output directory for Allure results
    allure_results_dir = "allure-results"

    # Ensure the allure-results directory exists and is empty before starting
    # This prevents old results from interfering
    if os.path.exists(allure_results_dir):
        import shutil
        shutil.rmtree(allure_results_dir)
    os.makedirs(allure_results_dir)

    # Base command arguments for Behave
    # -f allure_behave.formatter:AllureFormatter : Specifies the Allure formatter
    # -o allure-results : Specifies the output directory for Allure XML results
    # features/ : Specifies the directory where your feature files are located
    command_args = [
        "behave",
        "-f", "allure_behave.formatter:AllureFormatter",
        "-o", allure_results_dir,
        "features/" # Assuming your features are in a 'features' directory
    ]

    # Add browser argument if specified
    # You can change 'edge' to 'chrome' or 'firefox' here to run on different browsers
    # Or make it configurable via command line arguments to this script
    selected_browser = "edge" # Change this line to switch browsers via script
    if selected_browser:
        command_args.extend(["-D", f"browser={selected_browser}"])

    # Add tags if specified
    # This will run scenarios tagged with either @positive OR @negative
    # For AND logic (e.g., @smoke AND @regression), you'd use "--tags=@smoke --tags=@regression"
    # For OR logic (e.g., @smoke OR @regression), you'd use "--tags=@smoke,@regression"
    selected_tags = "@positive,@negative" # Change this line to filter by tags
    if selected_tags:
        command_args.extend(["--tags", selected_tags])

    print(f"Executing command: {' '.join(command_args)}")

    # Execute the Behave command
    try:
        subprocess.run(command_args, check=True)
        print("\nBehave tests executed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"\nERROR: Behave tests failed with exit code {e.returncode}")
    except FileNotFoundError:
        print("\nERROR: 'behave' command not found. Make sure Behave is installed and in your PATH.")

    # After tests run, you'll need to generate the HTML report using the Allure command-line tool.
    # This step is done separately, outside of this Python script, unless you want to
    # automate the Allure generation process here as well.
    print(f"\nAllure results saved to: {allure_results_dir}")
    print("To generate the Allure HTML report, run the following commands:")
    print(f"1. allure generate {allure_results_dir} --clean -o allure-report")
    print("2. allure open allure-report")
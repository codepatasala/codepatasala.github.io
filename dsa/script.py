import pandas as pd

# Read CSV


def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading CSV: {str(e)}")
        return None


# Generate HTML
def generate_html(df):
    html = """
    <!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Google tag (gtag.js) -->
    <script
      async
      src="https://www.googletagmanager.com/gtag/js?id=G-BNP01KFK5C"
    ></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      gtag("js", new Date());

      gtag("config", "G-BNP01KFK5C");
    </script>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Code Patasala - learn from the best</title>
    <link rel="icon" href="../images/favicon.png" type="image/x-icon" />
    <link
      rel="shortcut icon"
      href="../images/favicon.png"
      type="image/x-icon"
    />
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
    />
    <link rel="stylesheet" href="../styles/bootstrap-styles.css" />
  </head>
  <body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-light bg-dark">
      <a class="navbar-brand" href="https://codepatasala.com">
        <img
          src="../images/logo.png"
          width="30"
          height="30"
          class="d-inline-block align-top"
          alt="Logo"
        />
        CodePatasala
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <a class="nav-link" href="https://codepatasala.com">Home</a>
          </li>
          <li class="nav-item active">
            <a class="nav-link" href="https://codepatasala.com#courses"
              >Courses</a
            >
          </li>
          <li class="nav-item active">
            <a class="nav-link" href="https://codepatasala.com#youtube"
              >Youtube</a
            >
          </li>
          <li class="nav-item active">
            <a class="nav-link" href="https://codepatasala.com#contact"
              >Contact</a
            >
          </li>
        </ul>
      </div>
    </nav>

    <!-- Hero Section -->
    <header class="jumbotron text-center bg-primary text-dark">
      <h1 class="display-4">Welcome to CodePatasala</h1>
      <p class="lead">Your Placements Journey Starts Here</p>
    </header>

    <!-- Course Outline Section -->
    <section class="container py-5">
      <h2 class="text-center">DSA GRIND75 list</h2>

    """

    # Group by Week
    weeks = df['Week'].unique()
    for week in weeks:
        week_df = df[df['Week'] == week]
        html += f"""
          <!-- Week {week} -->
          <div class="accordion" id="week{week}">
        """

        # Generate cards for each problem
        for index, row in week_df.iterrows():
            print("Row:", row)
            html += f"""
              <div class="card">
                <div class="card-header" id="heading{index}">
                  <h5>
                    <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapse{index}" aria-expanded="false" aria-controls="collapse{index}">
                      Week {row['Week']}: {row['Summary']}
                    </button>
                    <div class="float-right">
                        <input type="checkbox" id="problem-checked-{index}" />
                        <label for="problem-checked-{index}"></label>
                    </div>
                  </h5>
                </div>
                <div id="collapse{index}" class="collapse" aria-labelledby="heading{index}" data-parent="#week{week}">
                  <div class="card-body">
                    <iframe width="560" height="315" src="{row['Video']}" title="YouTube video player" frameborder="0" allowfullscreen></iframe>
                    <p>
                      <b>Summary:</b> {row['Summary']}<br>
                      <b>Topics:</b> {row['Topics']}<br>
                      <b>Difficulty:</b> {row['Difficulty']}<br>
                      <b>Time:</b> {row['Time']}<br>
                      <b>Problem Link:</b> <a href="{row['URL']}">{row['URL']}</a>
                    </p>
                  </div>
                </div>
              </div>
            """

        html += """
          </div>
        """

    html += """
    </section>

    <!-- Footer -->
    <footer class="bg-dark text-dark text-center py-3">
      <p>&copy; 2023 CodePatasala. All rights reserved.</p>
    </footer>

        <!-- Bootstrap JS and jQuery -->
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        <script>
        $(document).ready(function() {
          $('input[type="checkbox"]').change(function() {
            var checkboxId = $(this).attr('id');
            var isChecked = $(this).is(':checked');
            localStorage.setItem(checkboxId, isChecked);
          });
          
          $('input[type="checkbox"]').each(function() {
            var checkboxId = $(this).attr('id');
            var checked = localStorage.getItem(checkboxId);
            if (checked === 'true') {
              $(this).prop('checked', true);
            }
          });
        });
      </script>
    </body>
    </html>
    """

    return html


# Main function
def main():
    csv_file = "problems.csv"  # Update with your CSV file path
    df = read_csv(csv_file)

    if df is not None:
        html = generate_html(df)
        with open("output.html", "w") as f:
            f.write(html)
        print("HTML generated successfully!")


if __name__ == "__main__":
    main()

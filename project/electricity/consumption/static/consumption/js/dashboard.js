
// =====================================
// ENERGY SYNC - DASHBOARD JAVASCRIPT
// =====================================


// 1. GET DATA FROM DJANGO

const labelsElement = document.getElementById("chart-labels");
const valuesElement = document.getElementById("chart-values");

const labels = labelsElement
    ? JSON.parse(labelsElement.textContent)
    : [];

const values = valuesElement
    ? JSON.parse(valuesElement.textContent)
    : [];


// 2. CREATE CONSUMPTION CHART

const chartCanvas = document.getElementById("usageChart");

let usageChart = null;

if (chartCanvas) {

    const ctx = chartCanvas.getContext("2d");

    usageChart = new Chart(ctx, {

        type: "bar",

        data: {

            labels: labels,

            datasets: [{

                label: "Electricity Usage (kWh)",

                data: values,

                backgroundColor: "#17633e",

                hoverBackgroundColor: "#38a66d",

                borderRadius: 12,

                borderSkipped: false,

                maxBarThickness: 35

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {
                    display: false
                },

                tooltip: {

                    backgroundColor: "#123c29",

                    padding: 12,

                    callbacks: {
                        label: function(context) {
                            return context.parsed.y + " kWh";
                        }
                    }

                }

            },

            scales: {

                x: {

                    grid: {
                        display: false
                    },

                    ticks: {
                        color: "#84918a",
                        font: {
                            size: 10
                        }
                    }

                },

                y: {

                    beginAtZero: true,

                    grid: {
                        color: "#edf1ee"
                    },

                    ticks: {
                        color: "#84918a",
                        font: {
                            size: 10
                        }
                    },

                    title: {
                        display: true,
                        text: "Energy (kWh)",
                        color: "#84918a"
                    }

                }

            }

        }

    });

}


// 3. CHANGE CHART TYPE

const chartTypeSelect = document.getElementById("chartType");

if (chartTypeSelect && usageChart) {

    chartTypeSelect.addEventListener("change", function() {

        usageChart.config.type = this.value;

        if (this.value === "line") {

            usageChart.data.datasets[0].backgroundColor = "#17633e";

            usageChart.data.datasets[0].borderColor = "#17633e";

            usageChart.data.datasets[0].pointBackgroundColor = "#17633e";

            usageChart.data.datasets[0].fill = false;

            usageChart.data.datasets[0].tension = 0.35;

            usageChart.data.datasets[0].borderWidth = 3;

        } else {

            usageChart.data.datasets[0].backgroundColor = "#17633e";

            usageChart.data.datasets[0].borderColor = "transparent";

            usageChart.data.datasets[0].fill = false;

            usageChart.data.datasets[0].borderWidth = 0;

        }

        usageChart.update();

    });

}


// 4. DARK MODE TOGGLE

const themeToggle = document.getElementById("themeToggle");

if (themeToggle) {

    themeToggle.addEventListener("click", function() {

        document.body.classList.toggle("dark-mode");

        const darkMode = document.body.classList.contains("dark-mode");

        themeToggle.textContent = darkMode ? "☀" : "☾";

        localStorage.setItem("energyTheme", darkMode ? "dark" : "light");

    });

    // Restore previously selected theme
    if (localStorage.getItem("energyTheme") === "dark") {

        document.body.classList.add("dark-mode");

        themeToggle.textContent = "☀";

    }

}


// 5. SEARCH RECENT CONSUMPTION RECORDS

const searchInput = document.getElementById("dashboardSearch");

if (searchInput) {

    searchInput.addEventListener("input", function() {

        const searchText = this.value.toLowerCase();

        const rows = document.querySelectorAll(
            ".recent-panel tbody tr"
        );

        rows.forEach(function(row) {

            row.style.display = row.textContent
                .toLowerCase()
                .includes(searchText) ? "" : "none";

        });

    });

}

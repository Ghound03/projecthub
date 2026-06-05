

setTimeout(() => {

    document
        .querySelectorAll(".alert")
        .forEach(alert => {

            const bsAlert =
                bootstrap.Alert.getOrCreateInstance(alert);

            bsAlert.close();

        });

}, 5000);

/*
 * Validate project dates.
 */

document.addEventListener("DOMContentLoaded", () => {

    const startDate =
        document.querySelector("#id_start_date");

    const endDate =
        document.querySelector("#id_end_date");

    if (!startDate || !endDate) {
        return;
    }

    endDate.addEventListener("change", () => {

        if (
            startDate.value &&
            endDate.value &&
            endDate.value < startDate.value
        ) {

            alert(
                "End date cannot be before the start date."
            );

            endDate.value = "";

        }

    });

});


/*
 * Highlight search box when user types.
 */

document.addEventListener("DOMContentLoaded", () => {

    const searchBox =
        document.querySelector(
            "input[name='search']"
        );

    if (!searchBox) {
        return;
    }

    searchBox.addEventListener("input", () => {

        if (searchBox.value.length > 0) {

            searchBox.classList.add(
                "border-primary"
            );

        } else {

            searchBox.classList.remove(
                "border-primary"
            );

        }

    });

});


/*
 * Dashboard chart.
 */

document.addEventListener("DOMContentLoaded", () => {

    const chartCanvas =
        document.getElementById(
            "projectStatusChart"
        );

    if (!chartCanvas) {
        return;
    }

    const planning =
        parseInt(
            chartCanvas.dataset.planning
        );

    const inProgress =
        parseInt(
            chartCanvas.dataset.inprogress
        );

    const completed =
        parseInt(
            chartCanvas.dataset.completed
        );

    const delayed =
        parseInt(
            chartCanvas.dataset.delayed
        );

    new Chart(chartCanvas, {

        type: "doughnut",

        data: {

            labels: [
                "Planning",
                "In Progress",
                "Completed",
                "Delayed"
            ],

            datasets: [{
                data: [
                    planning,
                    inProgress,
                    completed,
                    delayed
                ]
            }]
        }

    });

});
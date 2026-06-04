

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
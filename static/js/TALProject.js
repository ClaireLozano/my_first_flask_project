$(document).ready(function () {

	function init() {
		/*$('.btn-country-result').click(function(e) {
			$('.collapse-country-result').hide();
			console.log(e)
			//e.show();
		});*/
	};

	function createResultChart() {
		let percent = [];
		let country = [];

		for (let i = 0; i < data.data.length; i++) {
			percent.push(data.data[i][0]*100);
			country.push(data.data[i][1]);
		}

		createSimpleChart("result-chart", percent, country, '% de mots trouvés par pays', 100);
	};

	function createChartByCountry() {
		for (country in data.frequence) {
			let dataToDisplay = [];
			let labelToDisplay = [];

			for (let i = 0; i < data.frequence[country].length; i++) {
				dataToDisplay.push(data.frequence[country][i][0]);
				labelToDisplay.push(data.frequence[country][i][1]);
			}

			createSimpleChart("chart-result-details-" + country, dataToDisplay, labelToDisplay, 'Occurence');
		}
	};


	function createSimpleChart(idElement, dataToDisplay, labelToDisplay, label='', suggestedMax=100) {
		// do not resize the chart canvas when its container does (keep at 600x400px)
		Chart.defaults.global.responsive = false;

		// get chart canvas
		const ctx = document.getElementById(idElement).getContext("2d");

		// create the chart using the chart canvas
		const myChart = new Chart(ctx, {
			type: 'bar',
			data: {
				labels: labelToDisplay,
				datasets: [{
					label: label,
					data: dataToDisplay,
					borderWidth: 1
				}]
			},
			options: {
				scales: {
					yAxes: [{
						ticks: {
							beginAtZero: true,
							suggestedMin: 0,
							suggestedMax: suggestedMax
						}
					}]
				}
			}
		});

	};


	function createChartText() {
		let percent = [];
		let country = [];

		for (let i = 0; i < data.listSortedWords.length; i++) {
			percent.push(data.listSortedWords[i][0]);
			country.push(data.listSortedWords[i][1]);
		}

		createSimpleChart("chart-result-text-details", percent, country, 'Occurence', 20);
	};



	init();
	createResultChart();
	createChartByCountry();
	createChartText();

});
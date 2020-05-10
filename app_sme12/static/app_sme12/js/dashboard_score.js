$(function () {
    'use strict'
  
    var ticksStyle = {
      fontColor: '#495057',
      fontStyle: 'bold'
    }
  
    var mode      = 'index'
    var intersect = true
   
    var $salesChart = $('#sales-chart')
    var salesChart  = new Chart($salesChart, {
      type   : 'bar',
      data   : {
        labels  : ['หมวดที่ 1', 'หมวดที่ 2', 'หมวดที่ 3', 'หมวดที่ 4', 'หมวดที่ 5', 'หมวดที่ 6', 'หมวดที่ 7'],
        datasets: [
          {
            backgroundColor: '#007bff',
            borderColor    : '#007bff',
            data           : [85, 70, 90, 60, 70, 90, 90]
          },
          {
            backgroundColor: '#ced4da',
            borderColor    : '#ced4da',
            data           : [80, 80, 80, 80, 80, 80, 80]
          }
        ]
      },
      options: {
        maintainAspectRatio: false,
        tooltips           : {
          mode     : mode,
          intersect: intersect
        },
        hover              : {
          mode     : mode,
          intersect: intersect
        },
        legend             : {
          display: false
        },
        scales             : {
          yAxes: [{
            // display: false,
            gridLines: {
              display      : true,
              lineWidth    : '4px',
              color        : 'rgba(0, 0, 0, .2)',
              zeroLineColor: 'transparent'
            },
            ticks    : $.extend({
              beginAtZero: true,
  
              // Include a dollar sign in the ticks
              callback: function (value, index, values) {
                if (value >= 1000) {
                  value /= 1000
                  value += 'k'
                }
                return value + '%'
              }
            }, ticksStyle)
          }],
          xAxes: [{
            display  : true,
            gridLines: {
              display: false
            },
            ticks    : ticksStyle
          }]
        }
      }
    })
      
    //-------------
    //- PIE CHART -
    //-------------
    // Get context with jQuery - using jQuery's .get() method.
    var pieChartCanvas = $('#pieChart').get(0).getContext('2d')
    var pieChartCanvas2 = $('#pieChart2').get(0).getContext('2d')
    var pieChartCanvas3 = $('#pieChart3').get(0).getContext('2d')
    var pieData        = {
        labels: [
            'Chrome', 
            'IE',
            'FireFox', 
            'Safari', 
            'Opera', 
            'Navigator', 
        ],
        datasets: [
        {
            data: [700,500,400,600,300,100],
            backgroundColor : ['#f56954', '#00a65a', '#f39c12', '#00c0ef', '#3c8dbc', '#d2d6de'],
        }
        ]
    }
    var pieOptions     = {
        legend: {
        display: false
        }
    }
    //Create pie or douhnut chart
    // You can switch between pie and douhnut using the method below.
    var pieChart = new Chart(pieChartCanvas, {
        type: 'doughnut',
        data: pieData,
        options: pieOptions      
    })

    var pieChart2 = new Chart(pieChartCanvas2, {
        type: 'pie',
        data: pieData,
        options: pieOptions      
    })

    var pieChart3 = new Chart(pieChartCanvas3, {
        type: 'doughnut',
        data: pieData,
        options: pieOptions      
    })
    //-----------------
    //- END PIE CHART -
    //-----------------


  })
  
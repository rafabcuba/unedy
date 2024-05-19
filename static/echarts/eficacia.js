var chartDom = document.getElementById('container-eficacia');
var myChart = echarts.init(chartDom);
var colorPalette = ['#91cc75', '#ee6666']
var option;

option = {
  title: {
    text: 'Eficacia del trabajo',
    subtext: 'Taller',
    left: 'center'
  },
  tooltip: {
    trigger: 'item'
  },
  legend: {
    orient: 'vertical',
    left: 'left'
  },
  toolbox: {
    show: true,
    feature: {
      dataView: { readOnly: false },
      restore: {},
      saveAsImage: {}
    }
  },
  series: [
    {
      name: 'eficacia',
      type: 'pie',
      radius: '70%',
      color: colorPalette,
      data: [
        { value: solucionados, name: 'Solucionados' },
        { value: no_solucionados, name: 'No Solucionados' },
      ],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
};

option && myChart.setOption(option);
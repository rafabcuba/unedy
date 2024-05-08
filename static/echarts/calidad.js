var chartDom = document.getElementById('container-calidad');
var myChart = echarts.init(chartDom);
var colorPalette = ['#91cc75', '#ee6666']
var option;

option = {
  title: {
    text: 'Calidad de la información',
    subtext: 'ONEI',
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
      name: 'calidad',
      type: 'pie',
      radius: '70%',
      color: colorPalette,
      data: [
        { value: entiempoc, name: 'En tiempo' },
        { value: indisciplinasc, name: 'Indisciplinas' },
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
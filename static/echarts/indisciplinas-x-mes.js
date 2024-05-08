var chartDom = document.getElementById('container-indisciplinas-x-mes');
var myChart = echarts.init(chartDom);
var option;

option = {
  title: {
    text: 'Total de indisciplinas por mes'
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {},
  toolbox: {
    show: true,
    feature: {
      dataZoom: {
        yAxisIndex: 'none'
      },
      dataView: { readOnly: false },
      magicType: { type: ['line', 'bar'] },
      restore: {},
      saveAsImage: {}
    }
  },
  xAxis: {
    type: 'category',
    boundaryGap: false,
    data: meses
  },
  yAxis: {
    type: 'value',
    axisLabel: {
      formatter: '{value}'
    }
  },
  series: [
    {
      name: 'Indisciplinas',
      type: 'line',
      data: indisciplinasm,
      markPoint: {
        data: [
          { type: 'max', name: 'Max' },
          { type: 'min', name: 'Min' }
        ]
      },
      markLine: {
        data: [{ type: 'average', name: 'Avg' }]
      }
    }
  ]
};

option && myChart.setOption(option);

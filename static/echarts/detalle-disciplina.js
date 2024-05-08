var dom = document.getElementById('container-detalle-disciplina');
var myChart = echarts.init(dom, null, {
  renderer: 'canvas',
  useDirtyRect: false
});
var app = {};

var option;

option = {
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      // Use axis to trigger tooltip
      type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
    }
  },
  legend: {},
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
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
    type: 'value'
  },
  yAxis: {
    type: 'category',
    data: municipios
  },
  series: [
    {
      name: 'En tiempo',
      type: 'bar',
      stack: 'total',
      color: '#91cc75',
      label: {
        show: true
      },
      emphasis: {
        focus: 'series'
      },
      data: entiempo
    },
    {
      name: 'Indisciplinas',
      type: 'bar',
      stack: 'total',
      color: '#ee6666',
      label: {
        show: true
      },
      emphasis: {
        focus: 'series'
      },
      data: indisciplina
    }

  ]
};

if (option && typeof option === 'object') {
  myChart.setOption(option);
}

window.addEventListener('resize', myChart.resize);

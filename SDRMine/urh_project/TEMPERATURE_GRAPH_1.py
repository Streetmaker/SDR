options:
  parameters:
    author: ''
    category: '[GRC Hier Blocks]'
    cmake_opt: ''
    comment: ''
    copyright: ''
    description: ''
    gen_cmake: 'On'
    gen_linking: dynamic
    generate_options: qt_gui
    hier_block_src_path: '.:'
    id: Temp
    max_nouts: '0'
    output_language: python
    placement: (0,0)
    qt_qss_theme: ''
    realtime_scheduling: ''
    run: 'True'
    run_command: '{python} -u {filename}'
    run_options: prompt
    sizing_mode: fixed
    thread_safe_setters: ''
    title: Not titled yet
    window_size: ''
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [8, 8]
    rotation: 0
    state: enabled

blocks:
- name: samp_rate
  id: variable
  parameters:
    comment: ''
    value: '.5'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [184, 12]
    rotation: 0
    state: enabled
- name: blocks_vector_source_x_0
  id: blocks_vector_source_x
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    maxoutbuf: '0'
    minoutbuf: '0'
    repeat: 'False'
    tags: '[]'
    type: float
    vector: (52, 50, 48, 48, 46, 58, 63, 64, 67, 66, 63, 57, 0, 0, 0)
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [74, 147]
    rotation: 0
    state: true
- name: qtgui_time_sink_x_0
  id: qtgui_time_sink_x
  parameters:
    affinity: ''
    alias: ''
    alpha1: '1.0'
    alpha10: '1.0'
    alpha2: '1.0'
    alpha3: '1.0'
    alpha4: '1.0'
    alpha5: '1.0'
    alpha6: '1.0'
    alpha7: '1.0'
    alpha8: '1.0'
    alpha9: '1.0'
    autoscale: 'False'
    axislabels: 'True'
    color1: blue
    color10: dark blue
    color2: red
    color3: green
    color4: black
    color5: cyan
    color6: magenta
    color7: yellow
    color8: dark red
    color9: dark green
    comment: ''
    ctrlpanel: 'False'
    entags: 'True'
    grid: 'False'
    gui_hint: ''
    label1: Signal 1
    label10: Signal 10
    label2: Signal 2
    label3: Signal 3
    label4: Signal 4
    label5: Signal 5
    label6: Signal 6
    label7: Signal 7
    label8: Signal 8
    label9: Signal 9
    legend: 'True'
    marker1: '0'
    marker10: '-1'
    marker2: '-1'
    marker3: '-1'
    marker4: '-1'
    marker5: '-1'
    marker6: '-1'
    marker7: '-1'
    marker8: '-1'
    marker9: '-1'
    name: '"Temperatuer"'
    nconnections: '1'
    size: '12'
    srate: samp_rate
    stemplot: 'False'
    style1: '1'
    style10: '1'
    style2: '1'
    style3: '1'
    style4: '1'
    style5: '1'
    style6: '1'
    style7: '1'
    style8: '1'
    style9: '1'
    tr_chan: '0'
    tr_delay: '0'
    tr_level: '0.0'
    tr_mode: qtgui.TRIG_MODE_FREE
    tr_slope: qtgui.TRIG_SLOPE_POS
    tr_tag: '""'
    type: float
    update_time: '0.10'
    width1: '1'
    width10: '1'
    width2: '1'
    width3: '1'
    width4: '1'
    width5: '1'
    width6: '1'
    width7: '1'
    width8: '1'
    width9: '1'
    ylabel: ''
    ymax: '100'
    ymin: '0'
    yunit: '""'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [350, 146]
    rotation: 0
    state: true

connections:
- [blocks_vector_source_x_0, '0', qtgui_time_sink_x_0, '0']

metadata:
  file_format: 1

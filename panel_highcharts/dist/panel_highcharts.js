/*!
 * Copyright (c) 2012 - 2021, Anaconda, Inc., and Bokeh Contributors
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 * 
 * Redistributions of source code must retain the above copyright notice,
 * this list of conditions and the following disclaimer.
 * 
 * Redistributions in binary form must reproduce the above copyright notice,
 * this list of conditions and the following disclaimer in the documentation
 * and/or other materials provided with the distribution.
 * 
 * Neither the name of Anaconda nor the names of any contributors
 * may be used to endorse or promote products derived from this software
 * without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
 * THE POSSIBILITY OF SUCH DAMAGE.
 */
(function(root, factory) {
  factory(root["Bokeh"], undefined);
})(this, function(Bokeh, version) {
  let define;
  return (function(modules, entry, aliases, externals) {
    const bokeh = typeof Bokeh !== "undefined" && (version != null ? Bokeh[version] : Bokeh);
    if (bokeh != null) {
      return bokeh.register_plugin(modules, entry, aliases);
    } else {
      throw new Error("Cannot find Bokeh " + version + ". You have to load it prior to loading plugins.");
    }
  })
({
"0896b22af1": /* index.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    const tslib_1 = require("tslib");
    const HighChartsExtensions = (0, tslib_1.__importStar)(require("3c0c5c52d0") /* ./models/ */);
    exports.HighChartsExtensions = HighChartsExtensions;
    const base_1 = require("@bokehjs/base");
    (0, base_1.register_models)(HighChartsExtensions);
},
"3c0c5c52d0": /* models\index.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    var highchart_1 = require("df31ad65ef") /* ./highchart */;
    __esExport("HighChart", highchart_1.HighChart);
    var highstock_1 = require("60e97661a4") /* ./highstock */;
    __esExport("HighStock", highstock_1.HighStock);
    var highmap_1 = require("6d1e48a659") /* ./highmap */;
    __esExport("HighMap", highmap_1.HighMap);
    var highgantt_1 = require("dd1f1d4ad4") /* ./highgantt */;
    __esExport("HighGantt", highgantt_1.HighGantt);
},
"df31ad65ef": /* models\highchart.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    const highbase_1 = require("f43d669328") /* ./highbase */;
    class HighChartView extends highbase_1.HighBaseView {
        create_chart(wn, el, config) {
            return wn.Highcharts.chart(el, config);
        }
    }
    exports.HighChartView = HighChartView;
    HighChartView.__name__ = "HighChartView";
    class HighChart extends highbase_1.HighBase {
        static init_HighChart() {
            this.prototype.default_view = HighChartView;
        }
    }
    exports.HighChart = HighChart;
    HighChart.__name__ = "HighChart";
    HighChart.__module__ = "panel_highcharts.models.highchart";
    HighChart.init_HighChart();
},
"f43d669328": /* models\highbase.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    const html_box_1 = require("@bokehjs/models/layouts/html_box");
    class HighBaseView extends html_box_1.HTMLBoxView {
        connect_signals() {
            super.connect_signals();
            this.connect(this.model.properties.config.change, this.render);
            this.connect(this.model.properties.config_update.change, this._handle_config_update_change);
            this.connect(this.model.properties._add_series.change, this._add_series);
        }
        render() {
            super.render();
            if (this.chart) {
                this.chart.destroy();
            }
            const wn = window;
            if (wn.Highcharts) {
                const config = this._clean_config(this.model.config);
                this.chart = this.create_chart(wn, this.el, config);
            }
            else {
                console.error("HighCharts .js is not loaded. Could not create chart");
            }
        }
        create_chart(wn, el, config) {
            return wn.Highcharts.stockChart(el, config);
        }
        after_layout() {
            super.after_layout();
            this._resize();
        }
        _resize() {
            if (this.chart) {
                this.chart.reflow();
            }
        }
        _add_series() {
            if (this.chart) {
                const conf = this.model._add_series;
                conf.options = this._clean_config(conf.options);
                this.chart.addSeries(conf.options, conf.redraw, conf.animation);
            }
        }
        _handle_config_update_change() {
            const config_update = this._clean_config(this.model.config_update);
            this.chart.update(config_update);
        }
        _clean_config(config) {
            updateJS(config, this.model);
            return config;
        }
    }
    exports.HighBaseView = HighBaseView;
    HighBaseView.__name__ = "HighBaseView";
    class HighBase extends html_box_1.HTMLBox {
        constructor(attrs) {
            super(attrs);
        }
        static init_HighBase() {
            this.prototype.default_view = HighBaseView;
            this.define(({ Any }) => ({
                config: [Any],
                config_update: [Any],
                event: [Any],
                _add_series: [Any],
            }));
            this.override({
                height: 400,
                width: 600
            });
        }
    }
    exports.HighBase = HighBase;
    HighBase.__name__ = "HighBase";
    HighBase.__module__ = "panel_highcharts.models.highbase";
    HighBase.init_HighBase();
    // https://api.highcharts.com/highcharts/plotOptions.series.point.events.mouseOver
    function updateJS(config, model) {
        if (config === null) {
            return config;
        }
        for (var i = 0; i < Object.keys(config).length; i++) {
            const key = Object.keys(config)[i];
            const value = config[key];
            if (typeof value == "object") {
                updateJS(value, model);
            }
            else if (typeof value === "string" && value !== "") {
                if (value[0].charAt(0) === "@") {
                    const eventKey = value.slice(1, value.length);
                    config[key] = (event) => sendEvent(event, model, eventKey);
                }
                else if (value.startsWith('function') && value.indexOf("{") > -1 && value.lastIndexOf("}") > -1) {
                    const start = value.indexOf("{");
                    const end = value.lastIndexOf("}");
                    const command = value.slice(start + 1, end);
                    try {
                        config[key] = new Function(command);
                    }
                    catch (e) {
                        config[key] = null;
                        console.log("Could not set key '" + key + "' to function '" + command + "'. ", e);
                    }
                }
            }
        }
    }
    function sendEvent(event, model, key = null) {
        const eventData = filterEventData(event, key);
        // To make sure event gets sent we add a uuid
        // https://stackoverflow.com/questions/105034/how-to-create-a-guid-uuid
        eventData.uuid = uuidv4();
        model.event = eventData;
    }
    function filterEventData(event, channel = null) {
        const eventData = {};
        if (channel !== null && channel !== "") {
            eventData.channel = channel;
        }
        eventData.type = event.type;
        updateEventdata(event, eventData);
        return eventData;
    }
    function updateEventdata(event, eventData) {
        if (event.hasOwnProperty("index") && event["index"] !== undefined) {
            eventData.index = event["index"];
        }
        if (event.hasOwnProperty("name") && event["name"] !== undefined) {
            eventData.name = event["name"];
        }
        if (event.hasOwnProperty("x") && event.x !== undefined) {
            eventData.x = event.x;
        }
        if (event.hasOwnProperty("y") && event.y !== undefined) {
            eventData.y = event.y;
        }
        if (event.hasOwnProperty("target")) {
            eventData.target = {};
            updateEventdata(event.target, eventData.target);
        }
        if (event.hasOwnProperty("series")) {
            eventData.series = {};
            updateEventdata(event.series, eventData.series);
        }
        if (event.hasOwnProperty("point")) {
            eventData.point = {};
            updateEventdata(event.point, eventData.point);
        }
    }
    function uuidv4() {
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
            var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
        });
    }
},
"60e97661a4": /* models\highstock.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    const highbase_1 = require("f43d669328") /* ./highbase */;
    class HighStockView extends highbase_1.HighBaseView {
        create_chart(wn, el, config) {
            return wn.Highcharts.stockChart(el, config);
        }
    }
    exports.HighStockView = HighStockView;
    HighStockView.__name__ = "HighStockView";
    class HighStock extends highbase_1.HighBase {
        static init_HighStock() {
            this.prototype.default_view = HighStockView;
        }
    }
    exports.HighStock = HighStock;
    HighStock.__name__ = "HighStock";
    HighStock.__module__ = "panel_highcharts.models.highstock";
    HighStock.init_HighStock();
},
"6d1e48a659": /* models\highmap.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    const highbase_1 = require("f43d669328") /* ./highbase */;
    class HighMapView extends highbase_1.HighBaseView {
        create_chart(wn, el, config) {
            return wn.Highcharts.mapChart(el, config);
        }
    }
    exports.HighMapView = HighMapView;
    HighMapView.__name__ = "HighMapView";
    class HighMap extends highbase_1.HighBase {
        static init_HighMap() {
            this.prototype.default_view = HighMapView;
        }
    }
    exports.HighMap = HighMap;
    HighMap.__name__ = "HighMap";
    HighMap.__module__ = "panel_highcharts.models.highmap";
    HighMap.init_HighMap();
},
"dd1f1d4ad4": /* models\highgantt.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    const highbase_1 = require("f43d669328") /* ./highbase */;
    class HighGanttView extends highbase_1.HighBaseView {
        create_chart(wn, el, config) {
            return wn.Highcharts.ganttChart(el, config);
        }
    }
    exports.HighGanttView = HighGanttView;
    HighGanttView.__name__ = "HighGanttView";
    class HighGantt extends highbase_1.HighBase {
        static init_HighGantt() {
            this.prototype.default_view = HighGanttView;
        }
    }
    exports.HighGantt = HighGantt;
    HighGantt.__name__ = "HighGantt";
    HighGantt.__module__ = "panel_highcharts.models.highgantt";
    HighGantt.init_HighGantt();
},
}, "0896b22af1", {"index":"0896b22af1","models/index":"3c0c5c52d0","models/highchart":"df31ad65ef","models/highbase":"f43d669328","models/highstock":"60e97661a4","models/highmap":"6d1e48a659","models/highgantt":"dd1f1d4ad4"}, {});});
//# sourceMappingURL=panel_highcharts.js.map

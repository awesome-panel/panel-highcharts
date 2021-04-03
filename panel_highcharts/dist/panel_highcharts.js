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
  var define;
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
    const HighChartsExtensions = tslib_1.__importStar(require("3e9dd62cf5") /* ./models/ */);
    exports.HighChartsExtensions = HighChartsExtensions;
    const base_1 = require("@bokehjs/base");
    base_1.register_models(HighChartsExtensions);
},
"3e9dd62cf5": /* models\index.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    var highchart_1 = require("7c98d48d47") /* ./highchart */;
    __esExport("HighChart", highchart_1.HighChart);
},
"7c98d48d47": /* models\highchart.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    const html_box_1 = require("@bokehjs/models/layouts/html_box");
    class HighChartView extends html_box_1.HTMLBoxView {
        connect_signals() {
            super.connect_signals();
            this.connect(this.model.properties.config.change, this.render);
            this.connect(this.model.properties.config_update.change, this._handle_config_update_change);
        }
        render() {
            super.render();
            if (this.chart) {
                this.chart.destroy();
            }
            const wn = window;
            if (wn.Highcharts) {
                const config = this._clean_config(this.model.config);
                this.chart = wn.Highcharts.chart(this.el, config);
            }
            else {
                console.error("HighCharts .js is not loaded. Could not create chart");
            }
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
        _handle_config_update_change() {
            const config_update = this._clean_config(this.model.config_update);
            this.chart.update(config_update);
        }
        _clean_config(config) {
            updateJS(config, this.model);
            return config;
        }
    }
    exports.HighChartView = HighChartView;
    HighChartView.__name__ = "HighChartView";
    class HighChart extends html_box_1.HTMLBox {
        constructor(attrs) {
            super(attrs);
        }
        static init_HighChart() {
            this.prototype.default_view = HighChartView;
            this.define(({ Any }) => ({
                config: [Any],
                config_update: [Any],
                event: [Any],
            }));
            this.override({
                height: 400,
                width: 600
            });
        }
    }
    exports.HighChart = HighChart;
    HighChart.__name__ = "HighChart";
    HighChart.__module__ = "panel_highcharts.models.highchart";
    HighChart.init_HighChart();
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
            else if (typeof value === "string") {
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
}, "0896b22af1", {"index":"0896b22af1","models/index":"3e9dd62cf5","models/highchart":"7c98d48d47"}, {});});
//# sourceMappingURL=panel_highcharts.js.map

import * as p from "@bokehjs/core/properties"
import {HighBaseView, HighBase} from "./highbase"


export class HighChartView extends HighBaseView {
    create_chart(wn: any, el: HTMLElement, config: object): void {
      return wn.Highcharts.chart(el, config);
  }
}
export namespace HighChart {
  export type Attrs = p.AttrsOf<Props>
  export type Props = HighBase.Props
}

export interface HighChart extends HighBase.Attrs { }

export class HighChart extends HighBase {
    static __module__ = "panel_highcharts.models.highchart"

    static init_HighChart(): void {
      this.prototype.default_view = HighChartView;
    }
  }
import * as p from "@bokehjs/core/properties"
import {HighBaseView, HighBase} from "./highbase"


export class HighStockView extends HighBaseView {
    create_chart(wn: any, el: HTMLElement, config: object): void {
      return wn.Highcharts.stockChart(el, config);
  }
}
export namespace HighStock {
  export type Attrs = p.AttrsOf<Props>
  export type Props = HighBase.Props
}

export interface HighStock extends HighBase.Attrs { }

export class HighStock extends HighBase {
    static __module__ = "panel_highcharts.models.highstock"

    static init_HighStock(): void {
      this.prototype.default_view = HighStockView;
    }
  }
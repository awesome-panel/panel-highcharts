import * as p from "@bokehjs/core/properties"
import {HighBaseView, HighBase} from "./highbase"


export class HighMapView extends HighBaseView {
    create_chart(wn: any, el: HTMLElement, config: object): void {
      return wn.Highcharts.mapChart(el, config);
  }
}
export namespace HighMap {
  export type Attrs = p.AttrsOf<Props>
  export type Props = HighBase.Props
}

export interface HighMap extends HighBase.Attrs { }

export class HighMap extends HighBase {
    static __module__ = "panel_highcharts.models.highmap"

    static init_HighMap(): void {
      this.prototype.default_view = HighMapView;
    }
  }
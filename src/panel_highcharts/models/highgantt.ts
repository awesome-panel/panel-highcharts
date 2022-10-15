import * as p from "@bokehjs/core/properties"
import {HighBaseView, HighBase} from "./highbase"


export class HighGanttView extends HighBaseView {
    create_chart(wn: any, el: HTMLElement, config: object): void {
      return wn.Highcharts.ganttChart(el, config);
  }
}
export namespace HighGantt {
  export type Attrs = p.AttrsOf<Props>
  export type Props = HighBase.Props
}

export interface HighGantt extends HighBase.Attrs { }

export class HighGantt extends HighBase {
    static __module__ = "panel_highcharts.models.highgantt"

    static init_HighGantt(): void {
      this.prototype.default_view = HighGanttView;
    }
  }
import * as HighChartsExtensions from "./models/"
export {HighChartsExtensions}

import {register_models} from "@bokehjs/base"
register_models(HighChartsExtensions as any)
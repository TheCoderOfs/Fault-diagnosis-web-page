<template>
  <div class="app-container">
    <!-- <el-row>
      <el-col :span="24"><div class="grid-content bg-purple-dark"></div></el-col>
    </el-row>
    <el-row>
      <el-col :span="7"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="7"><div class="grid-content bg-purple-light"></div></el-col>
    </el-row> -->
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="预测数据">
        <el-upload
          class="upload-demo"
          drag
          :auto-upload="false"
          action="#"
          :on-change="uploadFile"
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip">
            只能上传csv/xls/txt文件，不超过500MB，且数据条数要大于100条<br>
            注：预测完成后要重新上传文件才能进行下一次预测！
          </div>
        </el-upload>
      </el-form-item>

      <el-form-item label="模型选择">
        <el-select
          v-model="form.modelname"
          placeholder="请选择预测模型"
          @focus="getChoiceList"
        >
          <!-- <el-option label="lightGBM" value="shanghai"></el-option>
        <el-option label="XGBoost" value="beijing"></el-option>
        <el-option label="GBDT" value="beijing"></el-option> -->
          <el-option
            v-for="item in options"
            :label="item.label"
            :value="item.value"
          ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">立即预测</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>

    <h2>预测结果：</h2>

    <el-row>
      <el-col :span="12">
        <el-table
          :data="list"
          element-loading-text="Loading"
          border
          fit
          highlight-current-row
          height="500"
        >
          <el-table-column align="center" label="ID" width="50">
            <template slot-scope="scope">
              {{ scope.$index }}
            </template>
          </el-table-column>
          <el-table-column label="sample_id">
            <template slot-scope="scope">
              {{ scope.row.sid }}
            </template>
          </el-table-column>
          <el-table-column label="预测label" width="150" align="center">
            <template slot-scope="scope">
              <span>{{ scope.row.label }}</span>
            </template>
          </el-table-column>
          <el-table-column label="置信度" width="200" align="center">
            <template slot-scope="scope">
              <span>{{ scope.row.confidence }}</span>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
      <el-col :span="12">
        <!-- <div class="grid-content bg-purple-light"></div> -->
        <div class="item" ref="PtWAWQntHtvI" style="height: 400px"></div>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import echarts from "echarts";
import "echarts-gl";
import { getList, getDataSetNames } from "@/api/dataset";
import { getModelNames } from "@/api/model";
import { predMulti } from "@/api/pred";
import { MessageBox, Message } from "element-ui";
export default {
  data() {
    return {
      list: [],
      options: [],
      options1: [],
      form: {
        formData: "",
        region: "",
      },
    };
  },
  methods: {
    // 上传文件
    uploadFile(item, fileList) {
      // console.log(item);
      let str = item.name
      let number = str.match(/\d+/)
      if (number[0]>=100) {
        this.formData = item.raw;
        // this.imageUrl = URL.createObjectURL(item.raw); // 图片上传浏览器回显地址
        // console.log(this.imageUrl, "imageUrl")
        // console.log(this.formData, "formData")
        // console.log(fileList);
        // 单个文件替换
        if (fileList.length > 1) {
          fileList.splice(0, 1);
        }
      }else{
        alert("数据条数小于100条")
        if (fileList.length > 1) {
          fileList.splice(1, 1);
        }else{
          fileList.splice(0, 1)
        }
      }

      
    },

    onSubmit() {
      // console.log('submit!');
      var formData = new FormData();
      formData.append("testfile", this.formData); // 照片文件
      formData.append("modelname", this.form.modelname); // 照片文件
      // formData.append("orderId", this.orderId);        // 其他参数
      predMulti(formData).then(
        (res) => {
          this.list = res.preds;
          this.initChart(res.data);
          console.log(res);
          Message({
            message: "预测成功",
            type: "success",
            duration: 5 * 1000,
          });
        },
        (err) => {
          // alert(err.message);
          console.log(err);
        }
      );
    },

    async getChoiceList() {
      let res = await getModelNames(this.parms);
      if (res && res.code == 20000) {
        console.log(res.data);
        this.options = res.options;
      }
    },
    // async getChoiceList1() {
    //   let res = await getDataSetNames(this.parms);
    //   if (res && res.code == 20000) {
    //     console.log(res.data);
    //     this.options1 = res.options;
    //   }
    // },

    initChart(data) {
      // this.chartColumn = echarts.init(this.$refs.chartColumn)
      // this.chartColumn.setOption(this.option)

      let goecharts_PtWAWQntHtvI = echarts.init(this.$refs.PtWAWQntHtvI);
      let colors = [
        "#5470c6",
        "#91cc75",
        "#fac858",
        "#ee6666",
        "#73c0de",
        "#3ba272",
        "#fc8452",
        "#9a60b4",
        "#ea7ccc",
      ];
      let data0 = data.data0;
      let data1 = data.data1;
      let data2 = data.data2;
      let data3 = data.data3;
      let data4 = data.data4;
      let data5 = data.data5;
      let option = {
        grid3D: {},
        xAxis3D: {},
        yAxis3D: {},
        zAxis3D: {},
        series: [
          {
            type: "scatter3D",
            data: data0,
            color: colors[0],
          },
          {
            type: "scatter3D",
            data: data1,
            color: colors[1],
          },
          {
            type: "scatter3D",
            data: data2,
            color: colors[2],
          },
          {
            type: "scatter3D",
            data: data3,
            color: colors[3],
          },
          {
            type: "scatter3D",
            data: data4,
            color: colors[4],
          },
          {
            type: "scatter3D",
            data: data5,
            color: colors[5],
          },
        ],
      };
      goecharts_PtWAWQntHtvI.setOption(option);
    },
  },
  mounted: function () {
    // this.initChart()
  },
};
</script>


<style>
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
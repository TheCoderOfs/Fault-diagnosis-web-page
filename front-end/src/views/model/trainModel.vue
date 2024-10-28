<template>
  <div class="app-container">
    <el-form
      v-loading="listLoading"
      ref="form"
      :model="form"
      label-width="80px"
    >
      <el-form-item label="模型名称">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="数据选择">
        <el-select
          v-model="form.data"
          placeholder="请选择模型训练数据"
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
      <el-form-item label="算法选择">
        <el-select v-model="form.region" placeholder="请选择模型训练算法">
          <el-option label="lightGBM" value="lightGBM"></el-option>
          <el-option label="XGBoost" value="XGBoost"></el-option>
          <!-- <el-option label="GBDT" value="beijing"></el-option> -->
        </el-select>
      </el-form-item>
      <!-- <el-form-item label="采集时间">
      <el-col :span="11">
        <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
      </el-col>
      <el-col class="line" :span="2">-</el-col>
      <el-col :span="11">
        <el-time-picker placeholder="采集时间" v-model="form.date2" style="width: 100%;"></el-time-picker>
      </el-col>
    </el-form-item> -->
      <!-- <el-form-item label="超参优化">
      <el-switch v-model="form.delivery"></el-switch>
    </el-form-item> -->
      <el-form-item label="训练选项">
        <el-checkbox-group v-model="form.type1">
          <el-checkbox label="Nan值补全" name="type1"></el-checkbox>
        </el-checkbox-group>
          <el-checkbox-group v-model="form.type2">
          <el-checkbox label="异常值处理" name="type2"></el-checkbox>
        </el-checkbox-group>
      </el-form-item>
      <!-- <el-form-item label="交叉验证">
      <el-radio-group v-model="form.resource">
        <el-radio label="无"></el-radio>
        <el-radio label="五折交叉验证"></el-radio>
        <el-radio label="十折交叉验证"></el-radio>
      </el-radio-group>
    </el-form-item> -->
      <el-form-item label="模型备注">
        <el-input type="textarea" v-model="form.desc"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">立即训练</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
import { getList, getDataSetNames } from "@/api/dataset";
import { trainModel } from "@/api/model";
import { MessageBox, Message } from "element-ui";
export default {
  data() {
    return {
      list: null,
      listLoading: false,
      options: [],
      form: {
        name: "",
        data: "",
        region: "",
        date1: "",
        date2: "",
        delivery: false,
        type1: "",
        type2:"",
        resource: "",
        desc: "",
      },
    };
  },
  created() {
    // this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true;
      getList().then((response) => {
        this.listLoading = false;

        // alert(response.code)
        // console.log(response)
        // this.list = response.data.items
      });
    },
    onSubmit() {
      var formData = new FormData();
      formData.append("dataset", this.form.data); // 数据文件
      formData.append("ALG", this.form.region); //算法名字
      formData.append("modelname", this.form.name); //模型名字
      formData.append("type1",this.form.type1) //按钮信息
      formData.append("type2",this.form.type2) //按钮信息
      trainModel(formData).then(
        (res) => {
          // alert(res.message);
          console.log(res);
          Message({
            message: res.message,
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
      let res = await getDataSetNames(this.parms);
      if (res && res.code == 20000) {
        console.log(res.data);
        this.options = res.options;
      }
    },
  },
};
</script>
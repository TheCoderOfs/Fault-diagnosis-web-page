<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="数据文件">
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
            只能上传csv/xls/txt文件，且不超过500Mb
          </div>
        </el-upload>
      </el-form-item>
      <!-- <el-form-item label="数据名称">
      <el-input v-model="form.name"></el-input>
    </el-form-item> -->
      <el-form-item label="数据格式">
        <el-select v-model="form.region" placeholder="请选择上传数据格式">
          <el-option label="csv" value="csv"></el-option>
          <el-option label="xls" value="xls"></el-option>
          <el-option label="txt" value="txt"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="采集时间">
        <el-col :span="11">
          <el-date-picker
            type="date"
            placeholder="选择日期"
            v-model="form.date1"
            style="width: 100%"
          ></el-date-picker>
        </el-col>
        <el-col class="line" :span="2">-</el-col>
        <el-col :span="11">
          <el-time-picker
            placeholder="采集时间"
            v-model="form.date2"
            style="width: 100%"
          ></el-time-picker>
        </el-col>
      </el-form-item>
      <el-form-item label="有Nan值">
        <el-switch v-model="form.delivery"></el-switch>
      </el-form-item>
      <!-- <el-form-item label="数据">
      <el-checkbox-group v-model="form.type">
        <el-checkbox label="美食/餐厅线上活动" name="type"></el-checkbox>
        <el-checkbox label="地推活动" name="type"></el-checkbox>
        <el-checkbox label="线下主题活动" name="type"></el-checkbox>
        <el-checkbox label="单纯品牌曝光" name="type"></el-checkbox>
      </el-checkbox-group>
    </el-form-item> -->
      <!--  <el-form-item label="数据格式">
      <el-radio-group v-model="form.resource">
        <el-radio label="csv"></el-radio>
        <el-radio label="xls"></el-radio>
        <el-radio label="txt"></el-radio>
      </el-radio-group> 
    </el-form-item>-->
      <el-form-item label="数据备注">
        <el-input type="textarea" v-model="form.desc"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">立即上传</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
import { uploadTrainDataSet } from "@/api/upload";
import { MessageBox, Message } from "element-ui";
export default {
  data() {
    return {
      form: {
        formData: "",
        region: "",
        delivery: true,
      },
    };
  },
  methods: {
    // 上传文件
    uploadFile(item, fileList) {
      this.formData = item.raw; // 图片文件
      // this.imageUrl = URL.createObjectURL(item.raw); // 图片上传浏览器回显地址
      // console.log(this.imageUrl, "imageUrl")
      // console.log(this.formData, "formData")
      // 单个文件替换
      if (fileList.length > 1) {
        fileList.splice(0, 1);
      }
    },

    onSubmit() {
      // console.log('submit!');
      
      var formData = new FormData();
      formData.append("file", this.formData); // 照片文件
      formData.append("NaN", this.form.delivery);
      // formData.append("orderId", this.orderId);        // 其他参数
      uploadTrainDataSet(formData).then(
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
    uploadSuccess(res, file, fileList) {
      alert("上传成功");
    },
    uploadError(res, file, fileList) {
      alert("上传失败");
    },
  },
};
</script>
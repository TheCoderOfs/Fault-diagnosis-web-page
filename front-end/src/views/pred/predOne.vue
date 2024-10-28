<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="80px">
    <el-form-item label="预测数据">
      <el-upload
        class="upload-demo"
        drag
        :auto-upload = false
        action="#"
        :on-change="uploadFile"
        >
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        <div class="el-upload__tip" slot="tip">只能上传csv/xls/txt文件，且不超过500Mb</div>
      </el-upload>
    </el-form-item>
    
    <el-form-item label="模型选择">
      <el-select v-model="form.modelname" placeholder="请选择预测模型"  @focus="getChoiceList">
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
    <el-form-item label="数据备注">
      <el-input type="textarea" v-model="form.desc"></el-input>
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="onSubmit">立即预测</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>

  </div>
</template>
<script>
import { getModelNames } from '@/api/model'
import { predOne } from '@/api/pred'
import { MessageBox, Message } from 'element-ui'
  export default {
    data() {
      return {
      	options: [],
        form: {
          formData: '',
          region: ''
        }
      }
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
        formData.append("testfile", this.formData);     // 照片文件
        formData.append("modelname", this.form.modelname);     // 照片文件
        // formData.append("orderId", this.orderId);        // 其他参数
        predOne(formData).then(res => {
          console.log(res);
          Message({
            message: res.res,
            type: 'success',
            duration: 5 * 1000
          })
        }, err => {
          // alert(err.message);
          console.log(err)
        })
      },
      uploadSuccess(res, file, fileList) {
        alert('上传成功');
      },
      uploadError(res, file, fileList) {
        alert('上传失败');
      },
      async getChoiceList(){
	    let res = await getModelNames(this.parms);
	    if (res && res.code == 20000) {
	      console.log(res.data);
	      this.options = res.options;
	    }
	  }
    }
  }
</script>
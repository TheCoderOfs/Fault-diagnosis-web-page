<template>
  <div class="app-container">
    <h2>当前系统已有模型：</h2>
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
    >
      <el-table-column align="center" label="ID" width="40">
        <template slot-scope="scope">
          {{ scope.$index }}
        </template>
      </el-table-column>
      <el-table-column label="模型名称">
        <template slot-scope="scope">
          {{ scope.row.modelname }}
        </template>
      </el-table-column>
      <!-- <el-table-column label="Accuracy" width="85" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.accuracy }}</span>
        </template>
      </el-table-column> -->
      <!-- <el-table-column label="Precision" width="85" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.precision }}</span>
        </template>
      </el-table-column> 
      <el-table-column label="Recall" width="85" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.recall }}</span>
        </template>
      </el-table-column> 
      <el-table-column label="F1" width="85" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.F1 }}</span>
        </template>
      </el-table-column> -->
      <el-table-column label="模型大小(MB)" width="85" align="center">
        <template slot-scope="scope">
          {{ scope.row.modelsize }}
        </template>
      </el-table-column>
      <!-- <el-table-column class-name="status-col" label="Status" width="110" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusFilter">{{ scope.row.status }}</el-tag>
        </template>
      </el-table-column> -->
      <el-table-column
        align="center"
        prop="created_at"
        label="创建时间"
        width="130"
      >
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.createtime }}</span>
        </template>
      </el-table-column>
      <el-table-column
        class-name="status-col"
        label="操作"
        width="150"
        align="center"
      >
        <template slot-scope="scope">
          <el-button
            class="item-btn"
            @click="downLoad(scope.row.modelname)"
            size="small"
            type="primary"
          >
            下载
          </el-button>
          <el-button
            class="item-btn"
            size="small"
            type="danger"
            @click="del(scope.row.modelname)"
          >
            删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { getList } from "@/api/model";
import { downloadModel } from "@/api/model";
import { MessageBox, Message } from "element-ui";

export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: "success",
        draft: "gray",
        deleted: "danger",
      };
      return statusMap[status];
    },
  },
  data() {
    return {
      list: null,
      listLoading: true,
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      this.listLoading = true;
      getList().then((response) => {
        this.list = response.data.items;
        this.listLoading = false;
      });
    },
    downLoad(modelname) {
      Message({
        message: "开始下载" + modelname,
        type: "success",
        duration: 5 * 1000,
      });
      window.location.href =
        "http://localhost:5003/download/model?modelname=" + modelname;
    },
    del(modelname) {
      // this.list.forEach(model => {
      //   if (model.modelname === modelname){
      //     this.list.pop(model)
      //     console.log(this.list);
      //   }
      // });
      if (confirm("确定删除吗？")) {
        for (let i = 0, len = this.list.length; i < len; i++) {
          if (this.list[i].modelname === modelname) {
            this.list.splice(i, 1); // console.log(this.list);
            break;
          }
        }
      }
    },
  },
};
</script>

<template>
  <div class="app-container">
    <p>当前系统数据集：</p>
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
    >
      <el-table-column align="center" label="ID" width="95">
        <template slot-scope="scope">
          {{ scope.$index }}
        </template>
      </el-table-column>
      <el-table-column label="数据集名称">
        <template slot-scope="scope">
          {{ scope.row.filename }}
        </template>
      </el-table-column>
      <el-table-column label="文件类型" width="150" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.filetype }}</span>
        </template>
      </el-table-column>
      <el-table-column label="文件大小(MB)" width="150" align="center">
        <template slot-scope="scope">
          {{ scope.row.filesize }}
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
        width="250"
      >
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.createtime }}</span>
        </template>
      </el-table-column>
      <el-table-column
        class-name="status-col"
        label="操作"
        width="110"
        align="center"
      >
        <template slot-scope="scope">
          <el-button
            class="item-btn"
            size="small"
            type="danger"
            @click="del(scope.row.filename)"
          >
            删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { getList } from "@/api/dataset";

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
    del(modelname) {
      // this.list.forEach(model => {
      //   if (model.modelname === modelname){
      //     this.list.pop(model)
      //     console.log(this.list);
      //   }
      // });
      if (confirm("确定删除吗？")) {
        for (let i = 0, len = this.list.length; i < len; i++) {
          if (this.list[i].filename === modelname) {
            this.list.splice(i, 1); // console.log(this.list);
            break;
          }
        }
      }
    },
  },
};
</script>

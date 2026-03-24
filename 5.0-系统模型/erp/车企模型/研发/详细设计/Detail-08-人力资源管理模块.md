# Detail-08 人力资源管理模块详细设计文档

## 文档信息

| 项目 | 内容 |
|------|------|
| 文档编号 | Detail-08 |
| 文档名称 | 人力资源管理模块详细设计文档 |
| 版本号 | V1.0 |
| 创建日期 | 2026-03-24 |
| 所属系统 | 汽车制造业ERP系统 |
| 技术栈 | Spring Boot 2.7 + MyBatis Plus |
| 关联PRD | PRD-08-人力资源管理模块 |

---

## 1. 系统架构设计

### 1.1 整体架构

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           前端层 (Vue 3.x)                               │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐        │
│  │   PC端      │ │  移动APP    │ │  小程序     │ │   H5页面    │        │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘        │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         API网关层 (Spring Cloud Gateway)                  │
│           统一鉴权 | 路由转发 | 限流熔断 | 日志记录                        │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           服务层 (Spring Boot 2.7)                       │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │                      HR微服务模块                                │    │
│  │  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐       │    │
│  │  │ 组织服务  │ │ 员工服务  │ │ 考勤服务  │ │ 薪资服务  │       │    │
│  │  └───────────┘ └───────────┘ └───────────┘ └───────────┘       │    │
│  │  ┌───────────┐ ┌───────────┐                                   │    │
│  │  │ 绩效服务  │ │ 培训服务  │                                   │    │
│  │  └───────────┘ └───────────┘                                   │    │
│  └─────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           数据层 (MyBatis Plus)                          │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐        │
│  │   MySQL     │ │   Redis     │ │ Elasticsearch│ │  文件存储   │        │
│  │  主数据库   │ │   缓存      │ │   搜索引擎   │ │   OSS       │        │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘        │
└─────────────────────────────────────────────────────────────────────────┘
```

### 1.2 模块依赖关系

```
                    ┌───────────────┐
                    │   组织管理    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   员工档案    │
                    └───────┬───────┘
                            │
            ┌───────────────┼───────────────┐
            │               │               │
            ▼               ▼               ▼
    ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
    │   考勤管理    │ │   绩效管理    │ │   培训管理    │
    └───────┬───────┘ └───────┬───────┘ └───────────────┘
            │               │
            └───────┬───────┘
                    │
                    ▼
            ┌───────────────┐
            │   薪资管理    │
            └───────────────┘
```

---

## 2. 包结构设计

### 2.1 模块包结构

```
com.autoerp.hr
├── common                      # 公共模块
│   ├── config                  # 配置类
│   │   ├── MybatisPlusConfig   # MyBatis Plus配置
│   │   ├── RedisConfig         # Redis配置
│   │   └── SecurityConfig      # 安全配置
│   ├── exception               # 异常类
│   │   ├── BusinessException   # 业务异常
│   │   └── GlobalExceptionHandler # 全局异常处理
│   ├── utils                   # 工具类
│   │   ├── EncryptUtils        # 加密工具
│   │   ├── ExcelUtils          # Excel工具
│   │   └── IdGenerator         # ID生成器
│   └── constants               # 常量类
│       ├── EmpConstants        # 员工常量
│       └── AttConstants        # 考勤常量
│
├── org                         # 组织管理模块
│   ├── controller              # 控制器
│   │   ├── DepartmentController
│   │   └── PositionController
│   ├── service                 # 服务接口
│   │   ├── DepartmentService
│   │   └── PositionService
│   ├── service.impl            # 服务实现
│   │   ├── DepartmentServiceImpl
│   │   └── PositionServiceImpl
│   ├── mapper                  # Mapper接口
│   │   ├── DepartmentMapper
│   │   └── PositionMapper
│   ├── entity                  # 实体类
│   │   ├── Department
│   │   └── Position
│   ├── dto                     # 数据传输对象
│   │   ├── DepartmentDTO
│   │   └── PositionDTO
│   └── vo                      # 视图对象
│       ├── DepartmentTreeVO
│       └── PositionVO
│
├── emp                         # 员工档案模块
│   ├── controller
│   ├── service
│   ├── mapper
│   ├── entity
│   ├── dto
│   └── vo
│
├── att                         # 考勤管理模块
│   ├── controller
│   ├── service
│   ├── mapper
│   ├── entity
│   ├── dto
│   └── vo
│
├── sal                         # 薪资管理模块
│   ├── controller
│   ├── service
│   ├── mapper
│   ├── entity
│   ├── dto
│   └── vo
│
├── per                         # 绩效管理模块
│   ├── controller
│   ├── service
│   ├── mapper
│   ├── entity
│   ├── dto
│   └── vo
│
└── trn                         # 培训管理模块
    ├── controller
    ├── service
    ├── mapper
    ├── entity
    ├── dto
    └── vo
```

---

## 3. 核心类设计

### 3.1 基础实体类

```java
/**
 * 基础实体类
 */
@Data
public class BaseEntity {
    /** 主键ID */
    @TableId(type = IdType.ASSIGN_ID)
    private Long id;

    /** 租户ID */
    private Long tenantId;

    /** 创建人 */
    @TableField(fill = FieldFill.INSERT)
    private Long createdBy;

    /** 创建时间 */
    @TableField(fill = FieldFill.INSERT)
    private LocalDateTime createdTime;

    /** 更新人 */
    @TableField(fill = FieldFill.UPDATE)
    private Long updatedBy;

    /** 更新时间 */
    @TableField(fill = FieldFill.UPDATE)
    private LocalDateTime updatedTime;

    /** 删除标记 */
    @TableLogic
    private Integer deleted;

    /** 版本号 */
    @Version
    private Integer version;
}
```

### 3.2 组织实体类

```java
/**
 * 组织单元实体
 */
@Data
@EqualsAndHashCode(callSuper = true)
@TableName("hr_org_department")
public class Department extends BaseEntity {
    /** 组织编码 */
    private String deptCode;

    /** 组织名称 */
    private String deptName;

    /** 组织英文名 */
    private String deptNameEn;

    /** 上级组织ID */
    private Long parentId;

    /** 组织类型 */
    private String deptType;

    /** 组织层级 */
    private Integer deptLevel;

    /** 组织路径 */
    private String deptPath;

    /** 负责人ID */
    private Long managerId;

    /** 成本中心 */
    private String costCenter;

    /** 利润中心 */
    private String profitCenter;

    /** 排序号 */
    private Integer sortOrder;

    /** 状态 */
    private Integer status;

    /** 备注 */
    private String remark;
}
```

### 3.3 员工实体类

```java
/**
 * 员工基本信息实体
 */
@Data
@EqualsAndHashCode(callSuper = true)
@TableName("hr_emp_employee")
public class Employee extends BaseEntity {
    /** 员工工号 */
    private String employeeNo;

    /** 员工姓名 */
    private String employeeName;

    /** 英文名 */
    private String employeeNameEn;

    /** 性别 */
    private String gender;

    /** 出生日期 */
    private LocalDate birthday;

    /** 证件类型 */
    private String idType;

    /** 证件号码(加密) */
    private String idNumber;

    /** 民族 */
    private String nation;

    /** 政治面貌 */
    private String politicalStatus;

    /** 婚姻状况 */
    private String maritalStatus;

    /** 籍贯 */
    private String nativePlace;

    /** 邮箱 */
    private String email;

    /** 手机号 */
    private String mobile;

    /** 固定电话 */
    private String phone;

    /** 家庭住址 */
    private String address;

    /** 紧急联系人 */
    private String emergencyContact;

    /** 紧急联系电话 */
    private String emergencyPhone;

    /** 照片URL */
    private String photoUrl;

    /** 所属部门ID */
    private Long deptId;

    /** 岗位ID */
    private Long positionId;

    /** 职级 */
    private String positionLevel;

    /** 员工类型 */
    private String employeeType;

    /** 员工状态 */
    private String employeeStatus;

    /** 入职日期 */
    private LocalDate hireDate;

    /** 转正日期 */
    private LocalDate regularDate;

    /** 工龄 */
    private BigDecimal workYears;

    /** 离职日期 */
    private LocalDate leaveDate;

    /** 离职原因 */
    private String leaveReason;

    /** 开户银行 */
    private String bankName;

    /** 银行账号(加密) */
    private String bankAccount;

    /** 备注 */
    private String remark;
}
```

### 3.4 考勤记录实体类

```java
/**
 * 考勤打卡记录实体
 */
@Data
@EqualsAndHashCode(callSuper = true)
@TableName("hr_att_record")
public class AttRecord extends BaseEntity {
    /** 员工ID */
    private Long employeeId;

    /** 打卡日期 */
    private LocalDate recordDate;

    /** 班次ID */
    private Long shiftId;

    /** 上班打卡时间 */
    private LocalTime onTime;

    /** 上班打卡状态 */
    private String onStatus;

    /** 上班打卡设备 */
    private String onDevice;

    /** 上班打卡位置 */
    private String onLocation;

    /** 上班打卡照片 */
    private String onPhotoUrl;

    /** 下班打卡时间 */
    private LocalTime offTime;

    /** 下班打卡状态 */
    private String offStatus;

    /** 下班打卡设备 */
    private String offDevice;

    /** 下班打卡位置 */
    private String offLocation;

    /** 下班打卡照片 */
    private String offPhotoUrl;

    /** 工作时长 */
    private BigDecimal workHours;

    /** 迟到分钟数 */
    private Integer lateMinutes;

    /** 早退分钟数 */
    private Integer earlyMinutes;

    /** 加班时长 */
    private BigDecimal overtimeHours;

    /** 考勤状态 */
    private String attStatus;

    /** 备注 */
    private String remark;
}
```

### 3.5 薪资核算实体类

```java
/**
 * 薪资核算主表实体
 */
@Data
@EqualsAndHashCode(callSuper = true)
@TableName("hr_sal_payroll")
public class SalPayroll extends BaseEntity {
    /** 工资单号 */
    private String payrollNo;

    /** 核算月份 */
    private String payrollMonth;

    /** 员工ID */
    private Long employeeId;

    /** 员工工号 */
    private String employeeNo;

    /** 员工姓名 */
    private String employeeName;

    /** 部门ID */
    private Long deptId;

    /** 部门名称 */
    private String deptName;

    /** 岗位名称 */
    private String positionName;

    /** 基本工资 */
    private BigDecimal baseSalary;

    /** 岗位工资 */
    private BigDecimal positionSalary;

    /** 绩效工资 */
    private BigDecimal performanceSalary;

    /** 加班费 */
    private BigDecimal overtimePay;

    /** 津贴补贴 */
    private BigDecimal allowance;

    /** 奖金 */
    private BigDecimal bonus;

    /** 计件工资 */
    private BigDecimal pieceSalary;

    /** 应发工资合计 */
    private BigDecimal grossSalary;

    /** 考勤扣款 */
    private BigDecimal absenceDeduct;

    /** 社保扣款 */
    private BigDecimal socialDeduct;

    /** 公积金扣款 */
    private BigDecimal housingFundDeduct;

    /** 个税扣款 */
    private BigDecimal taxDeduct;

    /** 其他扣款 */
    private BigDecimal otherDeduct;

    /** 实发工资 */
    private BigDecimal netSalary;

    /** 应出勤天数 */
    private BigDecimal workDays;

    /** 实际出勤天数 */
    private BigDecimal actualWorkDays;

    /** 加班小时 */
    private BigDecimal overtimeHours;

    /** 薪资明细JSON */
    private String salDetailJson;

    /** 状态 */
    private String status;

    /** 确认人 */
    private Long confirmBy;

    /** 确认时间 */
    private LocalDateTime confirmTime;

    /** 发放时间 */
    private LocalDateTime payTime;

    /** 备注 */
    private String remark;
}
```

---

## 4. 服务层设计

### 4.1 组织管理服务

```java
/**
 * 组织管理服务接口
 */
public interface DepartmentService extends IService<Department> {

    /**
     * 获取组织架构树
     */
    List<DepartmentTreeVO> getDepartmentTree(String deptType);

    /**
     * 创建组织单元
     */
    Long createDepartment(DepartmentDTO dto);

    /**
     * 更新组织单元
     */
    void updateDepartment(Long id, DepartmentDTO dto);

    /**
     * 删除组织单元
     */
    void deleteDepartment(Long id);

    /**
     * 获取组织详情
     */
    DepartmentVO getDepartmentDetail(Long id);

    /**
     * 调整组织层级
     */
    void adjustDepartment(Long id, Long newParentId);

    /**
     * 获取组织下所有员工
     */
    List<EmployeeVO> getDepartmentEmployees(Long deptId);
}

/**
 * 组织管理服务实现
 */
@Service
@RequiredArgsConstructor
public class DepartmentServiceImpl extends ServiceImpl<DepartmentMapper, Department>
        implements DepartmentService {

    private final EmployeeMapper employeeMapper;
    private final PositionMapper positionMapper;

    @Override
    @Cacheable(value = "department:tree", key = "#deptType")
    public List<DepartmentTreeVO> getDepartmentTree(String deptType) {
        LambdaQueryWrapper<Department> wrapper = new LambdaQueryWrapper<>();
        if (StrUtil.isNotBlank(deptType)) {
            wrapper.eq(Department::getDeptType, deptType);
        }
        wrapper.orderByAsc(Department::getSortOrder);

        List<Department> departments = this.list(wrapper);
        return buildDepartmentTree(departments, 0L);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    @CacheEvict(value = "department:tree", allEntries = true)
    public Long createDepartment(DepartmentDTO dto) {
        // 校验编码唯一性
        validateDeptCode(dto.getDeptCode(), null);

        Department department = BeanUtil.copyProperties(dto, Department.class);

        // 设置层级和路径
        if (dto.getParentId() != null && dto.getParentId() > 0) {
            Department parent = this.getById(dto.getParentId());
            department.setDeptLevel(parent.getDeptLevel() + 1);
            department.setDeptPath(parent.getDeptPath() + "/" + parent.getId());
        } else {
            department.setDeptLevel(1);
            department.setDeptPath("");
        }

        this.save(department);
        return department.getId();
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    @CacheEvict(value = "department:tree", allEntries = true)
    public void updateDepartment(Long id, DepartmentDTO dto) {
        Department department = this.getById(id);
        if (department == null) {
            throw new BusinessException("组织不存在");
        }

        // 编码不可修改
        BeanUtil.copyProperties(dto, department, "deptCode");
        this.updateById(department);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    @CacheEvict(value = "department:tree", allEntries = true)
    public void deleteDepartment(Long id) {
        // 检查是否有下级组织
        long childCount = this.count(new LambdaQueryWrapper<Department>()
                .eq(Department::getParentId, id));
        if (childCount > 0) {
            throw new BusinessException("该组织下存在子组织，无法删除");
        }

        // 检查是否有人员
        long employeeCount = employeeMapper.selectCount(new LambdaQueryWrapper<Employee>()
                .eq(Employee::getDeptId, id));
        if (employeeCount > 0) {
            throw new BusinessException("该组织下存在人员，无法删除");
        }

        // 检查是否有岗位
        long positionCount = positionMapper.selectCount(new LambdaQueryWrapper<Position>()
                .eq(Position::getDeptId, id));
        if (positionCount > 0) {
            throw new BusinessException("该组织下存在岗位，无法删除");
        }

        this.removeById(id);
    }

    /**
     * 构建组织树
     */
    private List<DepartmentTreeVO> buildDepartmentTree(List<Department> departments, Long parentId) {
        return departments.stream()
                .filter(d -> Objects.equals(d.getParentId(), parentId))
                .map(d -> {
                    DepartmentTreeVO vo = new DepartmentTreeVO();
                    BeanUtil.copyProperties(d, vo);

                    // 查询员工数量
                    long count = employeeMapper.selectCount(new LambdaQueryWrapper<Employee>()
                            .eq(Employee::getDeptId, d.getId()));
                    vo.setEmployeeCount((int) count);

                    // 递归构建子节点
                    vo.setChildren(buildDepartmentTree(departments, d.getId()));
                    return vo;
                })
                .collect(Collectors.toList());
    }

    /**
     * 校验组织编码唯一性
     */
    private void validateDeptCode(String deptCode, Long excludeId) {
        LambdaQueryWrapper<Department> wrapper = new LambdaQueryWrapper<Department>()
                .eq(Department::getDeptCode, deptCode);
        if (excludeId != null) {
            wrapper.ne(Department::getId, excludeId);
        }
        long count = this.count(wrapper);
        if (count > 0) {
            throw new BusinessException("组织编码已存在");
        }
    }
}
```

### 4.2 员工管理服务

```java
/**
 * 员工管理服务接口
 */
public interface EmployeeService extends IService<Employee> {

    /**
     * 分页查询员工列表
     */
    IPage<EmployeeVO> pageEmployees(EmployeeQueryDTO query);

    /**
     * 创建员工档案
     */
    Long createEmployee(EmployeeDTO dto);

    /**
     * 更新员工档案
     */
    void updateEmployee(Long id, EmployeeDTO dto);

    /**
     * 获取员工详情
     */
    EmployeeDetailVO getEmployeeDetail(Long id);

    /**
     * 办理入职
     */
    Long processEntry(EntryApplyDTO dto);

    /**
     * 办理离职
     */
    void processLeave(Long employeeId, LeaveApplyDTO dto);

    /**
     * 员工调动
     */
    void transferEmployee(TransferDTO dto);

    /**
     * 生成工号
     */
    String generateEmployeeNo();
}

/**
 * 员工管理服务实现
 */
@Service
@RequiredArgsConstructor
public class EmployeeServiceImpl extends ServiceImpl<EmployeeMapper, Employee>
        implements EmployeeService {

    private final EducationMapper educationMapper;
    private final WorkExperienceMapper workExperienceMapper;
    private final FamilyMemberMapper familyMemberMapper;
    private final ChangeRecordMapper changeRecordMapper;
    private final EncryptUtils encryptUtils;

    @Override
    public IPage<EmployeeVO> pageEmployees(EmployeeQueryDTO query) {
        Page<Employee> page = new Page<>(query.getPage(), query.getSize());

        LambdaQueryWrapper<Employee> wrapper = new LambdaQueryWrapper<>();

        // 工号查询
        if (StrUtil.isNotBlank(query.getEmployeeNo())) {
            wrapper.eq(Employee::getEmployeeNo, query.getEmployeeNo());
        }

        // 姓名模糊查询
        if (StrUtil.isNotBlank(query.getEmployeeName())) {
            wrapper.like(Employee::getEmployeeName, query.getEmployeeName());
        }

        // 部门筛选
        if (query.getDeptId() != null) {
            wrapper.eq(Employee::getDeptId, query.getDeptId());
        }

        // 状态筛选
        if (StrUtil.isNotBlank(query.getEmployeeStatus())) {
            wrapper.eq(Employee::getEmployeeStatus, query.getEmployeeStatus());
        }

        wrapper.orderByDesc(Employee::getCreatedTime);

        IPage<Employee> employeePage = this.page(page, wrapper);

        return employeePage.convert(this::convertToVO);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Long createEmployee(EmployeeDTO dto) {
        // 校验身份证号唯一性
        validateIdNumber(dto.getIdNumber(), null);

        Employee employee = new Employee();
        BeanUtil.copyProperties(dto, employee);

        // 自动生成工号
        if (StrUtil.isBlank(dto.getEmployeeNo())) {
            employee.setEmployeeNo(generateEmployeeNo());
        }

        // 加密敏感信息
        employee.setIdNumber(encryptUtils.encrypt(dto.getIdNumber()));
        if (StrUtil.isNotBlank(dto.getBankAccount())) {
            employee.setBankAccount(encryptUtils.encrypt(dto.getBankAccount()));
        }

        // 设置初始状态
        employee.setEmployeeStatus("PROBATION");
        employee.setWorkYears(BigDecimal.ZERO);

        this.save(employee);

        // 保存教育经历
        if (CollUtil.isNotEmpty(dto.getEducations())) {
            List<Education> educations = dto.getEducations().stream()
                    .map(e -> {
                        Education education = BeanUtil.copyProperties(e, Education.class);
                        education.setEmployeeId(employee.getId());
                        return education;
                    })
                    .collect(Collectors.toList());
            educationMapper.insertBatch(educations);
        }

        // 保存工作经历
        if (CollUtil.isNotEmpty(dto.getWorkExperiences())) {
            List<WorkExperience> experiences = dto.getWorkExperiences().stream()
                    .map(e -> {
                        WorkExperience experience = BeanUtil.copyProperties(e, WorkExperience.class);
                        experience.setEmployeeId(employee.getId());
                        return experience;
                    })
                    .collect(Collectors.toList());
            workExperienceMapper.insertBatch(experiences);
        }

        return employee.getId();
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void updateEmployee(Long id, EmployeeDTO dto) {
        Employee employee = this.getById(id);
        if (employee == null) {
            throw new BusinessException("员工不存在");
        }

        // 身份证号不可修改
        BeanUtil.copyProperties(dto, employee, "id", "employeeNo", "idNumber");

        // 加密敏感信息
        if (StrUtil.isNotBlank(dto.getBankAccount())) {
            employee.setBankAccount(encryptUtils.encrypt(dto.getBankAccount()));
        }

        this.updateById(employee);
    }

    @Override
    public EmployeeDetailVO getEmployeeDetail(Long id) {
        Employee employee = this.getById(id);
        if (employee == null) {
            throw new BusinessException("员工不存在");
        }

        EmployeeDetailVO vo = new EmployeeDetailVO();
        BeanUtil.copyProperties(employee, vo);

        // 解密敏感信息
        vo.setIdNumber(encryptUtils.maskIdNumber(employee.getIdNumber()));
        if (StrUtil.isNotBlank(employee.getBankAccount())) {
            vo.setBankAccount(encryptUtils.maskBankAccount(employee.getBankAccount()));
        }

        // 查询教育经历
        List<Education> educations = educationMapper.selectList(new LambdaQueryWrapper<Education>()
                .eq(Education::getEmployeeId, id)
                .orderByDesc(Education::getEndDate));
        vo.setEducations(educations);

        // 查询工作经历
        List<WorkExperience> experiences = workExperienceMapper.selectList(new LambdaQueryWrapper<WorkExperience>()
                .eq(WorkExperience::getEmployeeId, id)
                .orderByDesc(WorkExperience::getEndDate));
        vo.setWorkExperiences(experiences);

        // 查询家庭成员
        List<FamilyMember> familyMembers = familyMemberMapper.selectList(new LambdaQueryWrapper<FamilyMember>()
                .eq(FamilyMember::getEmployeeId, id));
        vo.setFamilyMembers(familyMembers);

        return vo;
    }

    @Override
    public String generateEmployeeNo() {
        // 格式: EMP + 年月 + 4位序号
        String prefix = "EMP" + DateUtil.format(new Date(), "yyyyMM");

        // 查询当月最大序号
        Integer maxSeq = this.baseMapper.getMaxSeqByPrefix(prefix);
        if (maxSeq == null) {
            maxSeq = 0;
        }

        return prefix + String.format("%04d", maxSeq + 1);
    }

    /**
     * 校验身份证号唯一性
     */
    private void validateIdNumber(String idNumber, Long excludeId) {
        String encryptedIdNumber = encryptUtils.encrypt(idNumber);

        LambdaQueryWrapper<Employee> wrapper = new LambdaQueryWrapper<Employee>()
                .eq(Employee::getIdNumber, encryptedIdNumber);
        if (excludeId != null) {
            wrapper.ne(Employee::getId, excludeId);
        }

        long count = this.count(wrapper);
        if (count > 0) {
            throw new BusinessException("身份证号已存在");
        }
    }

    /**
     * 转换为VO
     */
    private EmployeeVO convertToVO(Employee employee) {
        EmployeeVO vo = new EmployeeVO();
        BeanUtil.copyProperties(employee, vo);

        // 手机号脱敏
        vo.setMobile(encryptUtils.maskMobile(employee.getMobile()));

        return vo;
    }
}
```

### 4.3 考勤管理服务

```java
/**
 * 考勤管理服务接口
 */
public interface AttendanceService {

    /**
     * 打卡
     */
    ClockResultVO clock(ClockDTO dto);

    /**
     * 获取今日考勤状态
     */
    TodayStatusVO getTodayStatus(Long employeeId);

    /**
     * 提交请假申请
     */
    Long submitLeaveApply(LeaveApplyDTO dto);

    /**
     * 审批请假
     */
    void approveLeave(Long id, ApproveDTO dto);

    /**
     * 提交加班申请
     */
    Long submitOvertimeApply(OvertimeApplyDTO dto);

    /**
     * 获取考勤月报
     */
    AttMonthlyReportVO getMonthlyReport(String month, Long deptId);
}

/**
 * 考勤管理服务实现
 */
@Service
@RequiredArgsConstructor
public class AttendanceServiceImpl implements AttendanceService {

    private final AttRecordMapper attRecordMapper;
    private final AttScheduleMapper scheduleMapper;
    private final AttShiftMapper shiftMapper;
    private final LeaveApplyMapper leaveApplyMapper;
    private final LeaveBalanceMapper leaveBalanceMapper;
    private final EmployeeMapper employeeMapper;

    @Override
    @Transactional(rollbackFor = Exception.class)
    public ClockResultVO clock(ClockDTO dto) {
        // 查询员工
        Employee employee = employeeMapper.selectById(dto.getEmployeeId());
        if (employee == null) {
            throw new BusinessException("员工不存在");
        }

        // 查询当天排班
        LocalDate today = dto.getClockTime().toLocalDate();
        AttSchedule schedule = scheduleMapper.selectOne(new LambdaQueryWrapper<AttSchedule>()
                .eq(AttSchedule::getEmployeeId, dto.getEmployeeId())
                .eq(AttSchedule::getScheduleDate, today));

        if (schedule == null) {
            throw new BusinessException("当天无排班，无需打卡");
        }

        // 查询班次
        AttShift shift = shiftMapper.selectById(schedule.getShiftId());

        // 查询或创建考勤记录
        AttRecord record = attRecordMapper.selectOne(new LambdaQueryWrapper<AttRecord>()
                .eq(AttRecord::getEmployeeId, dto.getEmployeeId())
                .eq(AttRecord::getRecordDate, today));

        if (record == null) {
            record = new AttRecord();
            record.setEmployeeId(dto.getEmployeeId());
            record.setRecordDate(today);
            record.setShiftId(shift.getId());
        }

        LocalTime clockTime = dto.getClockTime().toLocalTime();
        ClockResultVO result = new ClockResultVO();

        // 判断打卡类型(上班/下班)
        if (dto.getClockType().equals("ON")) {
            // 上班打卡
            record.setOnTime(clockTime);
            record.setOnDevice(dto.getDeviceId());
            record.setOnLocation(dto.getLocation());
            record.setOnPhotoUrl(dto.getPhotoUrl());

            // 判断迟到
            LocalTime onTimeLimit = shift.getOnTime().plusMinutes(shift.getLateMinutes());
            if (clockTime.isAfter(onTimeLimit)) {
                record.setOnStatus("LATE");
                int lateMinutes = (int) Duration.between(shift.getOnTime(), clockTime).toMinutes();
                record.setLateMinutes(lateMinutes);
                result.setClockStatus("LATE");
                result.setMessage("打卡成功，迟到" + lateMinutes + "分钟");
            } else {
                record.setOnStatus("NORMAL");
                record.setLateMinutes(0);
                result.setClockStatus("NORMAL");
                result.setMessage("打卡成功");
            }
        } else {
            // 下班打卡
            record.setOffTime(clockTime);
            record.setOffDevice(dto.getDeviceId());
            record.setOffLocation(dto.getLocation());
            record.setOffPhotoUrl(dto.getPhotoUrl());

            // 判断早退
            LocalTime offTimeLimit = shift.getOffTime().minusMinutes(shift.getEarlyMinutes());
            if (clockTime.isBefore(offTimeLimit)) {
                record.setOffStatus("EARLY");
                int earlyMinutes = (int) Duration.between(clockTime, shift.getOffTime()).toMinutes();
                record.setEarlyMinutes(earlyMinutes);
                result.setClockStatus("EARLY");
                result.setMessage("打卡成功，早退" + earlyMinutes + "分钟");
            } else {
                record.setOffStatus("NORMAL");
                record.setEarlyMinutes(0);
                result.setClockStatus("NORMAL");
                result.setMessage("打卡成功");
            }

            // 计算工作时长
            if (record.getOnTime() != null) {
                BigDecimal workHours = calculateWorkHours(record.getOnTime(), clockTime, shift);
                record.setWorkHours(workHours);
            }
        }

        // 保存或更新记录
        if (record.getId() == null) {
            attRecordMapper.insert(record);
        } else {
            attRecordMapper.updateById(record);
        }

        result.setClockTime(dto.getClockTime());
        result.setShiftName(shift.getShiftName());

        return result;
    }

    @Override
    public TodayStatusVO getTodayStatus(Long employeeId) {
        LocalDate today = LocalDate.now();

        // 查询排班
        AttSchedule schedule = scheduleMapper.selectOne(new LambdaQueryWrapper<AttSchedule>()
                .eq(AttSchedule::getEmployeeId, employeeId)
                .eq(AttSchedule::getScheduleDate, today));

        TodayStatusVO vo = new TodayStatusVO();
        vo.setDate(today);

        if (schedule == null) {
            vo.setShiftName("无排班");
            return vo;
        }

        AttShift shift = shiftMapper.selectById(schedule.getShiftId());
        vo.setShiftName(shift.getShiftName());
        vo.setOnTime(shift.getOnTime());
        vo.setOffTime(shift.getOffTime());

        // 查询打卡记录
        AttRecord record = attRecordMapper.selectOne(new LambdaQueryWrapper<AttRecord>()
                .eq(AttRecord::getEmployeeId, employeeId)
                .eq(AttRecord::getRecordDate, today));

        if (record != null) {
            vo.setOnClockTime(record.getOnTime());
            vo.setOnClockStatus(record.getOnStatus());
            vo.setOffClockTime(record.getOffTime());
            vo.setOffClockStatus(record.getOffStatus());
            vo.setWorkHours(record.getWorkHours());
        }

        return vo;
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Long submitLeaveApply(LeaveApplyDTO dto) {
        // 查询假期余额
        LeaveBalance balance = leaveBalanceMapper.selectOne(new LambdaQueryWrapper<LeaveBalance>()
                .eq(LeaveBalance::getEmployeeId, dto.getEmployeeId())
                .eq(LeaveBalance::getLeaveTypeId, dto.getLeaveTypeId())
                .eq(LeaveBalance::getYear, LocalDate.now().getYear()));

        // 检查余额
        if (balance != null && balance.getRemainingDays().compareTo(dto.getLeaveDays()) < 0) {
            throw new BusinessException("假期余额不足");
        }

        // 创建请假申请
        LeaveApply apply = new LeaveApply();
        BeanUtil.copyProperties(dto, apply);
        apply.setApplyNo(generateApplyNo("LE"));
        apply.setStatus("PENDING");

        leaveApplyMapper.insert(apply);

        return apply.getId();
    }

    /**
     * 计算工作时长
     */
    private BigDecimal calculateWorkHours(LocalTime onTime, LocalTime offTime, AttShift shift) {
        // 计算总时长
        long totalMinutes = Duration.between(onTime, offTime).toMinutes();

        // 扣除休息时间
        if (shift.getRestStartTime() != null && shift.getRestEndTime() != null) {
            // 判断休息时间是否在工作时间内
            if (!shift.getRestStartTime().isBefore(onTime) && !shift.getRestEndTime().isAfter(offTime)) {
                long restMinutes = Duration.between(shift.getRestStartTime(), shift.getRestEndTime()).toMinutes();
                totalMinutes -= restMinutes;
            }
        }

        return BigDecimal.valueOf(totalMinutes).divide(BigDecimal.valueOf(60), 1, RoundingMode.HALF_UP);
    }

    /**
     * 生成申请单号
     */
    private String generateApplyNo(String prefix) {
        return prefix + DateUtil.format(new Date(), "yyyyMMddHHmmss") + RandomUtil.randomNumbers(4);
    }
}
```

### 4.4 薪资核算服务

```java
/**
 * 薪资核算服务接口
 */
public interface SalaryService {

    /**
     * 执行薪资核算
     */
    PayrollResultVO calculatePayroll(PayrollCalculateDTO dto);

    /**
     * 获取工资单列表
     */
    IPage<PayrollVO> pagePayroll(PayrollQueryDTO query);

    /**
     * 获取工资单详情
     */
    PayrollDetailVO getPayrollDetail(Long id);

    /**
     * 审核工资单
     */
    void confirmPayroll(Long id);

    /**
     * 发放工资
     */
    void paySalary(Long id);

    /**
     * 计算个税
     */
    BigDecimal calculateTax(BigDecimal taxableIncome, BigDecimal accumulatedTaxable);

    /**
     * 计算社保
     */
    SocialResultVO calculateSocial(Long employeeId, BigDecimal salaryBase);
}

/**
 * 薪资核算服务实现
 */
@Service
@RequiredArgsConstructor
public class SalaryServiceImpl implements SalaryService {

    private final SalPayrollMapper payrollMapper;
    private final EmployeeSalaryMapper employeeSalaryMapper;
    private final EmployeeSocialMapper employeeSocialMapper;
    private final SocialSchemeMapper socialSchemeMapper;
    private final AttRecordMapper attRecordMapper;
    private final PerRecordMapper perRecordMapper;
    private final EmployeeMapper employeeMapper;

    @Override
    @Transactional(rollbackFor = Exception.class)
    public PayrollResultVO calculatePayroll(PayrollCalculateDTO dto) {
        String payrollMonth = dto.getPayrollMonth();

        // 查询核算范围内的员工
        List<Employee> employees = getCalculationEmployees(dto);

        PayrollResultVO result = new PayrollResultVO();
        result.setPayrollMonth(payrollMonth);
        result.setTotalEmployee(employees.size());

        int successCount = 0;
        List<PayrollFailVO> failList = new ArrayList<>();

        for (Employee employee : employees) {
            try {
                // 计算单个员工薪资
                calculateEmployeePayroll(employee, payrollMonth);
                successCount++;
            } catch (Exception e) {
                PayrollFailVO fail = new PayrollFailVO();
                fail.setEmployeeId(employee.getId());
                fail.setEmployeeName(employee.getEmployeeName());
                fail.setReason(e.getMessage());
                failList.add(fail);
            }
        }

        result.setSuccessCount(successCount);
        result.setFailCount(employees.size() - successCount);
        result.setFailList(failList);

        return result;
    }

    /**
     * 计算单个员工薪资
     */
    private void calculateEmployeePayroll(Employee employee, String payrollMonth) {
        // 查询员工薪资档案
        EmployeeSalary salary = employeeSalaryMapper.selectOne(new LambdaQueryWrapper<EmployeeSalary>()
                .eq(EmployeeSalary::getEmployeeId, employee.getId())
                .eq(EmployeeSalary::getStatus, 1)
                .le(EmployeeSalary::getEffectDate, LocalDate.now())
                .orderByDesc(EmployeeSalary::getEffectDate)
                .last("LIMIT 1"));

        if (salary == null) {
            throw new BusinessException("员工薪资档案不存在");
        }

        // 查询考勤数据
        BigDecimal workDays = getWorkDays(payrollMonth);
        BigDecimal actualWorkDays = getActualWorkDays(employee.getId(), payrollMonth);
        BigDecimal overtimeHours = getOvertimeHours(employee.getId(), payrollMonth);

        // 查询绩效数据
        BigDecimal performanceRate = getPerformanceRate(employee.getId(), payrollMonth);

        // 计算应发工资
        BigDecimal baseSalary = salary.getBaseSalary();
        BigDecimal positionSalary = salary.getPositionSalary();
        BigDecimal performanceSalary = salary.getPerformanceSalary().multiply(performanceRate);
        BigDecimal overtimePay = calculateOvertimePay(baseSalary, overtimeHours);

        BigDecimal grossSalary = baseSalary.add(positionSalary)
                .add(performanceSalary).add(overtimePay);

        // 计算扣款
        BigDecimal absenceDeduct = calculateAbsenceDeduct(baseSalary, workDays, actualWorkDays);
        SocialResultVO social = calculateSocial(employee.getId(), baseSalary);
        BigDecimal taxDeduct = calculateTax(employee.getId(), grossSalary, payrollMonth);

        // 计算实发工资
        BigDecimal netSalary = grossSalary.subtract(absenceDeduct)
                .subtract(social.getPersonalTotal()).subtract(taxDeduct);

        // 保存工资单
        SalPayroll payroll = new SalPayroll();
        payroll.setPayrollNo(generatePayrollNo(payrollMonth));
        payroll.setPayrollMonth(payrollMonth);
        payroll.setEmployeeId(employee.getId());
        payroll.setEmployeeNo(employee.getEmployeeNo());
        payroll.setEmployeeName(employee.getEmployeeName());
        payroll.setDeptId(employee.getDeptId());
        payroll.setBaseSalary(baseSalary);
        payroll.setPositionSalary(positionSalary);
        payroll.setPerformanceSalary(performanceSalary);
        payroll.setOvertimePay(overtimePay);
        payroll.setGrossSalary(grossSalary);
        payroll.setAbsenceDeduct(absenceDeduct);
        payroll.setSocialDeduct(social.getPersonalTotal());
        payroll.setTaxDeduct(taxDeduct);
        payroll.setNetSalary(netSalary);
        payroll.setWorkDays(workDays);
        payroll.setActualWorkDays(actualWorkDays);
        payroll.setOvertimeHours(overtimeHours);
        payroll.setStatus("CALCULATED");

        payrollMapper.insert(payroll);
    }

    @Override
    public BigDecimal calculateTax(BigDecimal taxableIncome, BigDecimal accumulatedTaxable) {
        // 累计应纳税所得额
        BigDecimal totalTaxable = accumulatedTaxable.add(taxableIncome);

        // 税率表（简化版）
        BigDecimal tax;
        if (totalTaxable.compareTo(BigDecimal.valueOf(36000)) <= 0) {
            tax = totalTaxable.multiply(BigDecimal.valueOf(0.03));
        } else if (totalTaxable.compareTo(BigDecimal.valueOf(144000)) <= 0) {
            tax = totalTaxable.multiply(BigDecimal.valueOf(0.10)).subtract(BigDecimal.valueOf(2520));
        } else if (totalTaxable.compareTo(BigDecimal.valueOf(300000)) <= 0) {
            tax = totalTaxable.multiply(BigDecimal.valueOf(0.20)).subtract(BigDecimal.valueOf(16920));
        } else if (totalTaxable.compareTo(BigDecimal.valueOf(420000)) <= 0) {
            tax = totalTaxable.multiply(BigDecimal.valueOf(0.25)).subtract(BigDecimal.valueOf(31920));
        } else if (totalTaxable.compareTo(BigDecimal.valueOf(660000)) <= 0) {
            tax = totalTaxable.multiply(BigDecimal.valueOf(0.30)).subtract(BigDecimal.valueOf(52920));
        } else {
            tax = totalTaxable.multiply(BigDecimal.valueOf(0.45)).subtract(BigDecimal.valueOf(181920));
        }

        return tax.setScale(2, RoundingMode.HALF_UP);
    }

    @Override
    public SocialResultVO calculateSocial(Long employeeId, BigDecimal salaryBase) {
        // 查询员工社保信息
        EmployeeSocial employeeSocial = employeeSocialMapper.selectOne(new LambdaQueryWrapper<EmployeeSocial>()
                .eq(EmployeeSocial::getEmployeeId, employeeId)
                .eq(EmployeeSocial::getStatus, "NORMAL"));

        if (employeeSocial == null) {
            return new SocialResultVO();
        }

        // 查询社保方案
        SocialScheme scheme = socialSchemeMapper.selectById(employeeSocial.getSocialSchemeId());

        // 计算各项社保
        BigDecimal socialBase = employeeSocial.getSocialBase();
        BigDecimal pension = socialBase.multiply(scheme.getPensionPersonRate());
        BigDecimal medical = socialBase.multiply(scheme.getMedicalPersonRate());
        BigDecimal unemployment = socialBase.multiply(scheme.getUnemploymentPersonRate());

        BigDecimal housingFundBase = employeeSocial.getHousingFundBase();
        BigDecimal housingFund = housingFundBase.multiply(scheme.getHousingFundPersonRate());

        SocialResultVO result = new SocialResultVO();
        result.setPension(pension);
        result.setMedical(medical);
        result.setUnemployment(unemployment);
        result.setHousingFund(housingFund);
        result.setPersonalTotal(pension.add(medical).add(unemployment).add(housingFund));

        return result;
    }

    /**
     * 计算加班费
     */
    private BigDecimal calculateOvertimePay(BigDecimal baseSalary, BigDecimal overtimeHours) {
        // 时薪 = 基本工资 / 21.75 / 8
        BigDecimal hourlyRate = baseSalary.divide(BigDecimal.valueOf(21.75), 2, RoundingMode.HALF_UP)
                .divide(BigDecimal.valueOf(8), 2, RoundingMode.HALF_UP);

        // 加班费 = 时薪 * 加班时长 * 1.5倍（工作日）
        return hourlyRate.multiply(overtimeHours).multiply(BigDecimal.valueOf(1.5))
                .setScale(2, RoundingMode.HALF_UP);
    }

    /**
     * 生成工资单号
     */
    private String generatePayrollNo(String payrollMonth) {
        return "PAY" + payrollMonth.replace("-", "") + RandomUtil.randomNumbers(6);
    }
}
```

---

## 5. 流程设计

### 5.1 入职流程

```
┌─────────────────────────────────────────────────────────────────────────┐
│                            员工入职流程                                  │
└─────────────────────────────────────────────────────────────────────────┘

    ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
    │ 招聘系统 │────>│ 发起入职 │────>│ 资料收集 │────>│ 入职审批 │
    │ 候选人   │     │ 申请     │     │          │     │          │
    └──────────┘     └──────────┘     └──────────┘     └────┬─────┘
                                                             │
                         ┌───────────────────────────────────┤
                         │                                   │
                         ▼                                   ▼
                  ┌──────────┐                        ┌──────────┐
                  │ 驳回     │                        │ 通过     │
                  │ 通知修改 │                        │          │
                  └──────────┘                        └────┬─────┘
                                                           │
                         ┌─────────────────────────────────┼─────────────────┐
                         │                                 │                 │
                         ▼                                 ▼                 ▼
                  ┌──────────┐                      ┌──────────┐      ┌──────────┐
                  │ 创建档案 │                      │ 签订合同 │      │ 开通账号 │
                  └────┬─────┘                      └──────────┘      └──────────┘
                       │
                       ▼
                ┌──────────┐     ┌──────────┐
                │ 员工定薪 │────>│ 入职培训 │
                └──────────┘     └──────────┘
```

### 5.2 薪资核算流程

```
┌─────────────────────────────────────────────────────────────────────────┐
│                            薪资核算流程                                  │
└─────────────────────────────────────────────────────────────────────────┘

    ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
    │ 确认考勤 │────>│ 确认绩效 │────>│ 执行核算 │────>│ 核算预览 │
    │ 数据     │     │ 数据     │     │          │     │          │
    └──────────┘     └──────────┘     └──────────┘     └────┬─────┘
                                                           │
                         ┌─────────────────────────────────┤
                         │                                 │
                         ▼                                 ▼
                  ┌──────────┐                      ┌──────────┐
                  │ 异常处理 │                      │ 审核确认 │
                  └──────────┘                      └────┬─────┘
                                                         │
                         ┌───────────────────────────────┼───────────────┐
                         │                               │               │
                         ▼                               ▼               ▼
                  ┌──────────┐                    ┌──────────┐    ┌──────────┐
                  │ 生成代发 │                    │ 发送工资 │    │ 财务凭证 │
                  │ 文件     │                    │ 条       │    │          │
                  └────┬─────┘                    └──────────┘    └──────────┘
                       │
                       ▼
                ┌──────────┐     ┌──────────┐
                │ 银行代发 │────>│ 发放确认 │
                └──────────┘     └──────────┘
```

---

## 6. 定时任务设计

### 6.1 定时任务列表

| 任务名称 | Cron表达式 | 说明 |
|----------|------------|------|
| 合同到期提醒 | 0 0 8 * * ? | 每天8点检查30天内到期合同 |
| 生日提醒 | 0 0 9 * * ? | 每天9点检查当天生日员工 |
| 考勤异常提醒 | 0 30 9 * * ? | 每天9:30检查昨日考勤异常 |
| 薪资核算提醒 | 0 0 9 25 * ? | 每月25日提醒薪资核算 |
| 假期余额更新 | 0 0 0 1 1 ? | 每年1月1日重置年假余额 |
| 培训提醒 | 0 0 8 * * ? | 每天8点提醒当日培训 |
| 试用期转正提醒 | 0 0 9 * * ? | 每天9点检查7天内到期试用期 |

### 6.2 定时任务实现

```java
/**
 * HR定时任务
 */
@Component
@RequiredArgsConstructor
public class HrScheduledTasks {

    private final ContractMapper contractMapper;
    private final EmployeeMapper employeeMapper;
    private final MessageService messageService;

    /**
     * 合同到期提醒
     */
    @Scheduled(cron = "0 0 8 * * ?")
    public void contractExpiryReminder() {
        // 查询30天内到期合同
        LocalDate today = LocalDate.now();
        LocalDate expiryDate = today.plusDays(30);

        List<Contract> contracts = contractMapper.selectList(new LambdaQueryWrapper<Contract>()
                .eq(Contract::getStatus, "EFFECTIVE")
                .between(Contract::getEndDate, today, expiryDate));

        for (Contract contract : contracts) {
            Employee employee = employeeMapper.selectById(contract.getEmployeeId());

            // 发送提醒消息
            MessageDTO message = new MessageDTO();
            message.setTitle("合同到期提醒");
            message.setContent(String.format("员工%s的合同将于%s到期，请及时处理续签事宜。",
                    employee.getEmployeeName(), contract.getEndDate()));
            message.setReceiverId(employee.getId());

            messageService.sendMessage(message);
        }
    }

    /**
     * 生日提醒
     */
    @Scheduled(cron = "0 0 9 * * ?")
    public void birthdayReminder() {
        LocalDate today = LocalDate.now();
        int month = today.getMonthValue();
        int day = today.getDayOfMonth();

        // 查询当天生日员工
        List<Employee> employees = employeeMapper.selectList(new LambdaQueryWrapper<Employee>()
                .apply("MONTH(birthday) = {0}", month)
                .apply("DAY(birthday) = {0}", day)
                .eq(Employee::getEmployeeStatus, "REGULAR"));

        for (Employee employee : employees) {
            // 发送生日祝福
            MessageDTO message = new MessageDTO();
            message.setTitle("生日祝福");
            message.setContent("祝您生日快乐！");
            message.setReceiverId(employee.getId());

            messageService.sendMessage(message);
        }
    }
}
```

---

## 7. 缓存设计

### 7.1 缓存策略

| 数据类型 | 缓存策略 | 过期时间 | 说明 |
|----------|----------|----------|------|
| 组织架构树 | 本地缓存 | 30分钟 | 变更时清除 |
| 员工基本信息 | Redis | 1小时 | 变更时清除 |
| 岗位列表 | Redis | 1小时 | 变更时清除 |
| 薪资等级 | Redis | 1天 | 变更时清除 |
| 社保方案 | Redis | 1天 | 变更时清除 |
| 数据字典 | Redis | 1天 | 变更时清除 |

### 7.2 缓存Key设计

```
# 组织架构
department:tree:{tenantId}:{deptType}

# 员工信息
employee:info:{tenantId}:{employeeId}

# 岗位列表
position:list:{tenantId}:{deptId}

# 薪资等级
salary:grade:{tenantId}

# 社保方案
social:scheme:{tenantId}:{schemeId}

# 数据字典
dict:{dictType}
```

---

## 8. 消息队列设计

### 8.1 消息队列使用场景

| 场景 | 队列名称 | 消费者 | 说明 |
|------|----------|--------|------|
| 入职成功 | hr.entry.success | 账号服务、通知服务 | 开通账号、发送通知 |
| 离职成功 | hr.leave.success | 账号服务、门禁服务 | 停用账号、取消门禁 |
| 薪资发放 | hr.salary.pay | 通知服务 | 发送工资条 |
| 考勤异常 | hr.attendance.exception | 通知服务 | 发送异常提醒 |
| 绩效发布 | hr.performance.publish | 通知服务 | 发送绩效通知 |

### 8.2 消息格式

```json
{
  "messageId": "MSG001",
  "messageType": "HR_ENTRY_SUCCESS",
  "timestamp": "2024-06-01T10:00:00",
  "data": {
    "employeeId": 1,
    "employeeNo": "EMP001",
    "employeeName": "张三",
    "deptId": 1,
    "positionId": 1,
    "hireDate": "2024-06-01"
  }
}
```

---

## 9. 安全设计

### 9.1 数据加密

```java
/**
 * 加密工具类
 */
@Component
public class EncryptUtils {

    private static final String AES_KEY = "your-aes-secret-key";

    /**
     * AES加密
     */
    public String encrypt(String plainText) {
        if (StrUtil.isBlank(plainText)) {
            return null;
        }
        try {
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
            SecretKeySpec keySpec = new SecretKeySpec(AES_KEY.getBytes(), "AES");
            IvParameterSpec ivSpec = new IvParameterSpec(AES_KEY.substring(0, 16).getBytes());
            cipher.init(Cipher.ENCRYPT_MODE, keySpec, ivSpec);
            byte[] encrypted = cipher.doFinal(plainText.getBytes(StandardCharsets.UTF_8));
            return Base64.getEncoder().encodeToString(encrypted);
        } catch (Exception e) {
            throw new RuntimeException("加密失败", e);
        }
    }

    /**
     * AES解密
     */
    public String decrypt(String encryptedText) {
        if (StrUtil.isBlank(encryptedText)) {
            return null;
        }
        try {
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
            SecretKeySpec keySpec = new SecretKeySpec(AES_KEY.getBytes(), "AES");
            IvParameterSpec ivSpec = new IvParameterSpec(AES_KEY.substring(0, 16).getBytes());
            cipher.init(Cipher.DECRYPT_MODE, keySpec, ivSpec);
            byte[] decrypted = cipher.doFinal(Base64.getDecoder().decode(encryptedText));
            return new String(decrypted, StandardCharsets.UTF_8);
        } catch (Exception e) {
            throw new RuntimeException("解密失败", e);
        }
    }

    /**
     * 手机号脱敏
     */
    public String maskMobile(String mobile) {
        if (StrUtil.isBlank(mobile) || mobile.length() < 7) {
            return mobile;
        }
        return mobile.substring(0, 3) + "****" + mobile.substring(mobile.length() - 4);
    }

    /**
     * 身份证号脱敏
     */
    public String maskIdNumber(String idNumber) {
        if (StrUtil.isBlank(idNumber) || idNumber.length() < 8) {
            return idNumber;
        }
        return idNumber.substring(0, 4) + "**********" + idNumber.substring(idNumber.length() - 4);
    }

    /**
     * 银行账号脱敏
     */
    public String maskBankAccount(String account) {
        if (StrUtil.isBlank(account) || account.length() < 8) {
            return account;
        }
        return account.substring(0, 4) + "********" + account.substring(account.length() - 4);
    }
}
```

### 9.2 权限控制

```java
/**
 * 数据权限拦截器
 */
@Component
public class DataPermissionInterceptor implements InnerInterceptor {

    @Override
    public void beforeQuery(Executor executor, MappedStatement ms, Object parameter, RowBounds rowBounds, ResultHandler resultHandler, BoundSql boundSql) {
        // 获取当前用户
        LoginUser loginUser = SecurityUtils.getLoginUser();
        if (loginUser == null) {
            return;
        }

        // 获取租户ID
        Long tenantId = loginUser.getTenantId();

        // 获取SQL
        String sql = boundSql.getSql();

        // 添加租户条件
        if (sql.toLowerCase().contains("tenant_id")) {
            sql = sql.replaceAll("(?i)where", "WHERE tenant_id = " + tenantId + " AND");
        } else {
            sql = sql + " WHERE tenant_id = " + tenantId;
        }

        // 如果不是管理员，添加部门权限
        if (!loginUser.isAdmin()) {
            List<Long> deptIds = loginUser.getDeptIds();
            if (CollUtil.isNotEmpty(deptIds)) {
                sql = sql + " AND dept_id IN (" + CollUtil.join(deptIds, ",") + ")";
            }
        }

        // 更新SQL
        PluginUtils.MPBoundSql mpBs = PluginUtils.mpBoundSql(boundSql);
        mpBs.sql(sql);
    }
}
```

---

## 10. 异常处理

### 10.1 异常类设计

```java
/**
 * 业务异常
 */
public class BusinessException extends RuntimeException {
    private Integer code;
    private String message;

    public BusinessException(String message) {
        super(message);
        this.code = 500;
        this.message = message;
    }

    public BusinessException(Integer code, String message) {
        super(message);
        this.code = code;
        this.message = message;
    }
}

/**
 * 全局异常处理
 */
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(BusinessException.class)
    public Result<Void> handleBusinessException(BusinessException e) {
        return Result.fail(e.getCode(), e.getMessage());
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public Result<Void> handleValidationException(MethodArgumentNotValidException e) {
        String message = e.getBindingResult().getFieldErrors().stream()
                .map(FieldError::getDefaultMessage)
                .collect(Collectors.joining(", "));
        return Result.fail(400, message);
    }

    @ExceptionHandler(Exception.class)
    public Result<Void> handleException(Exception e) {
        log.error("系统异常", e);
        return Result.fail(500, "系统异常，请联系管理员");
    }
}
```

---

## 11. 日志设计

### 11.1 操作日志

```java
/**
 * 操作日志注解
 */
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface OperationLog {
    String module();
    String operation();
}

/**
 * 操作日志切面
 */
@Aspect
@Component
@RequiredArgsConstructor
public class OperationLogAspect {

    private final OperationLogMapper operationLogMapper;

    @Around("@annotation(operationLog)")
    public Object around(ProceedingJoinPoint point, OperationLog operationLog) throws Throwable {
        long startTime = System.currentTimeMillis();

        OperationLogEntity logEntity = new OperationLogEntity();
        logEntity.setModule(operationLog.module());
        logEntity.setOperation(operationLog.operation());
        logEntity.setRequestTime(LocalDateTime.now());

        // 获取请求参数
        Object[] args = point.getArgs();
        logEntity.setRequestParams(JSON.toJSONString(args));

        try {
            Object result = point.proceed();
            logEntity.setStatus(1);
            logEntity.setResponseResult(JSON.toJSONString(result));
            return result;
        } catch (Exception e) {
            logEntity.setStatus(0);
            logEntity.setErrorMsg(e.getMessage());
            throw e;
        } finally {
            logEntity.setExecutionTime(System.currentTimeMillis() - startTime);
            operationLogMapper.insert(logEntity);
        }
    }
}
```

---

## 12. 性能优化

### 12.1 数据库优化

- 合理使用索引，避免全表扫描
- 分页查询使用 LIMIT
- 批量操作使用批量插入
- 复杂查询使用 EXPLAIN 分析

### 12.2 缓存优化

- 热点数据使用 Redis 缓存
- 本地缓存使用 Caffeine
- 缓存穿透使用布隆过滤器
- 缓存雪崩使用随机过期时间

### 12.3 代码优化

- 避免在循环中查询数据库
- 使用异步处理耗时操作
- 使用连接池管理数据库连接
- 合理使用线程池

---

**文档审批**

| 角色 | 姓名 | 日期 | 签名 |
|------|------|------|------|
| 架构师 | | | |
| 技术负责人 | | | |
| 开发负责人 | | | |
var approval_limit_data = new Array();
var validate_add_attributes = [];
var main_table_low_value = [];
var approval_limit={};

//onclick of upload button display id_data_upload popup and set GLOBAL_ACTION button value
function onclick_upload_button() {
    GLOBAL_ACTION = "approval_limit_upload"
    $("#id_popup_tbody").empty();
    $('#id_data_upload').modal('show');
    document.getElementById('id_file_data_upload').value = "";
}

// on click update icon display the selected checkbox data to update
function onclick_update_button() {
    GLOBAL_ACTION = "UPDATE"
    onclick_copy_update_button("update")
    document.getElementById("id_del_add_button").style.display = "none";
}

//onclick of cancel empty the popup table body and error messages
$(".remove_upload_data").click(() => {
    $("#id_error_msg").html("");
    $("#id_popup_tbody").empty();
    $("#id_error_msg").empty();
    $('#myModal').modal('hide');
    $("#id_error_msg").prop("hidden", true);
    $("#id_error_msg_approval_limit_code").prop("hidden", true);
    $("#id_error_msg_approval_limit_name").prop("hidden", true);
    $("#id_error_msg_approval_limit_length").prop("hidden", true);
    $("#id_check_error_messages").prop("hidden", true);
    $("#id_check_success_messages").prop("hidden", true);
    $("#id_check_special_character_messages").prop("hidden", true)
    $("#id_check_data").prop("hidden", true);
    $('#id_popup_table').DataTable().destroy();
});

// on click add icon display the row in to add the new entries
function add_popup_row() {
$("#error_msg_id").css("display", "none")
    basic_add_new_html = '';
    var display_db_data = '';
    $('#id_popup_table').DataTable().destroy();
    $(".modal").on("hidden.bs.modal", function() {
        $("#id_error_msg").html("");
    });
    new_row_data();   // Add a new row in popup
    var company_num = '';
    $("#id_popup_table TBODY TR").each(function () {
        var row = $(this);
        row.find("TD").eq(3).find("select").empty()
        company_num = row.find("TD").eq(1).find("select option:selected").val();
        var assign_val = approval_limit_find(company_num)
        row.find("TD").eq(3).find("select").append(assign_val.app_code_id_dropdown)
        $(row.find("TD").eq(1).find("select")).change(function () {
              company_dropdwn_change(row);
        })
    })
    if (GLOBAL_ACTION == "UPLOAD") {
        $(".class_del_checkbox").prop("hidden", false);
    }
}

//onclick of cancel display the table in display mode............
function display_basic_db_data() {
    $('#display_basic_table').DataTable().destroy();
    $('#id_approval_limit_tbody').empty();
    var edit_basic_data = '';
    $.each(rendered_approval_limit_data, function(i, item) {
        edit_basic_data += '<tr ><td class="class_select_checkbox"><input class="checkbox_check" onclick="valueChanged()" type="checkbox" required></td><td>' + item.company_id + '</td><td>' + item.approver_username + '</td><td>' + item.app_code_id + '</td><td hidden>' + item.app_guid + '</td></tr>';
    });
    $('#id_approval_limit_tbody').append(edit_basic_data);
    $("#hg_select_checkbox").prop("hidden", true);
    $(".class_select_checkbox").prop("hidden", true);
    $('input:checkbox').removeAttr('checked');
    $('#id_edit_data').show();
    $('#id_cancel_data').hide();
    $('#id_delete_data').hide();
    $('#id_copy_data').hide();
    $('#id_update_data').hide();
    $('#id_save_confirm_popup').modal('hide');
    $('#id_delete_confirm_popup').modal('hide');
    $('#id_check_all').hide();
    table_sort_filter('display_basic_table');
}

//*****************************
function delete_duplicate() {
    $('#id_popup_table').DataTable().destroy();
    var approval_limit_code_check = new Array
    $("#id_popup_table TBODY TR").each(function() {
        var row = $(this);

        //*************** reading data from the pop-up ***************
        aapprover_username = row.find("TD").eq(2).find('input[type="text"]').val().toUpperCase();
        company_id = row.find("TD").eq(1).find("select option:selected").val();
        app_code_id = row.find("TD").eq(3).find("select option:selected").val();  
        app_guid = row.find("TD").eq(4).find('input[type="text"]').val().toUpperCase()
        approval_limit_compare = approver_username +'-'+ company_id +'-'+ app_code_id 
        if (approval_limit_code_check.includes(approval_limit_compare)) {
            $(row).remove();
        }
        approval_limit_code_check.push(approval_limit_compare);
    })
    table_sort_filter_popup('id_popup_table')
    check_data()
}

// Functtion to hide and display save related popups
$('#save_id').click(function () {
    $('#myModal').modal('hide');
    approval_limit_data = read_popup_data();
    $('#id_save_confirm_popup').modal('show');
});

//Read popup table data
function read_popup_data() {
    validate_add_attributes = [];
    var approval_limit={};
    $("#id_popup_table TBODY TR").each(function () {
        var row = $(this);
        approval_limit = {};
        approval_limit.del_ind = row.find("TD").eq(5).find('input[type="checkbox"]').is(':checked');
        approval_limit.approver_username = row.find("TD").eq(2).find("select option:selected").val();
        approval_limit.company_id = row.find("TD").eq(1).find("select option:selected").val();
        approval_limit.app_code_id = row.find("TD").eq(3).find("select option:selected").val();
        approval_limit.app_guid = row.find("TD").eq(4).find('input[type="text"]').val().toUpperCase()
        var approval_limit_compare = approval_limit.approver_username +'-'+ approval_limit.company_id +'-'+ approval_limit.app_code_id
        if (approval_limit == undefined) {
            approval_limit.approver_username = row.find("TD").eq(1).find("select option:selected").val();
        }
        if(approval_limit.app_guid == undefined) {
                approval_limit.app_guid = ''
            }
        validate_add_attributes.push(approval_limit_compare);
        approval_limit_data.push(approval_limit);
    });
    return approval_limit_data;
}

function display_error_message(error_message){
    $('#error_message').text(error_message);
    document.getElementById("error_message").style.color = "Red";
    $("#error_msg_id").css("display", "block")
    $('#id_save_confirm_popup').modal('hide');
    $('#myModal').modal('show');
}

// Function for add a new row data
function new_row_data() {
    basic_add_new_html = '<tr><td><input type="checkbox" required></td><td><select class="form-control" type="text">'+company_id_dropdown+'</select></td><td><select class="form-control" type="text">'+user_name_dropdown+'</select></td><td><select class="form-control" type="text">'+app_code_id_dropdown+'</select></td><td hidden><input type="text" value=""></td><td class="class_del_checkbox" hidden><input type="checkbox" required></td></tr>';
    $('#id_popup_tbody').append(basic_add_new_html);
    table_sort_filter('id_popup_table');
}

// Function to get main table data
function get_main_table_data() {
    main_table_low_value = [];
    $("#display_basic_table TBODY TR").each(function() {
        var row = $(this);
        var main_attribute = {};
        main_attribute.approver_username = row.find("TD").eq(2).html();
        main_attribute.company_id = row.find("TD").eq(1).html();
        main_attribute.app_code_id = row.find("TD").eq(3).html();
        var approval_limit_compare_maintable = main_attribute.approver_username +'-'+main_attribute.company_id +'-'+ main_attribute.app_code_id
        main_table_low_value.push(approval_limit_compare_maintable);
    });
    table_sort_filter('display_basic_table');
}

// Function to get the selected row data
function get_selected_row_data() {
    $("#display_basic_table TBODY TR").each(function() {
        var row = $(this);
        var approval_limit_arr_obj = {};
        approval_limit_arr_obj.del_ind = row.find("TD").eq(0).find('input[type="checkbox"]').is(':checked');
        if(approval_limit_arr_obj.del_ind){
        approval_limit_arr_obj.approver_username = row.find("TD").eq(2).html();
        approval_limit_arr_obj.company_id = row.find("TD").eq(1).html();
        approval_limit_arr_obj.app_code_id = row.find("TD").eq(3).html();
        approval_limit_arr_obj.app_guid = row.find("TD").eq(4).html();
        main_table_approval_limit_checked.push(approval_limit_arr_obj);
        }
    });
}
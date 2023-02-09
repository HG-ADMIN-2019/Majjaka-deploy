var transaction_types_data = new Array();
var validate_add_attributes = [];
var TransactionTypes={};

// on click add icon display the row in to add the new entries
function add_popup_row() {
    dropdown_value();
    $("#error_msg_id").css("display", "none")
    basic_add_new_html = '';
    var display_db_data = '';
    $('#id_popup_table').DataTable().destroy();
    $(".modal").on("hidden.bs.modal", function () {
        $("#id_error_msg").html("");
    });
    eliminate_used_sequence()
    basic_add_new_html = '<tr><td><input type="checkbox" required></td><td><input class="input form-control check_special_char" type="text" maxlength="15"  name="transaction type" style="text-transform:uppercase;" required></td><td><input type="text" class="form-control check_special_char" maxlength="10"  name="transaction description"  required></td><td><select class="input form-control" disabled>'+ document_type_dropdown +'</select></td><td><select class="input form-control">' + sequence_dropdown + '</select></td><td><input type="checkbox"  name="active_inactive" required></td><td hidden><input type="text" class= "form-control" name=" guid "></td><td hidden><input type="checkbox" required></td></tr>';

    $('#id_popup_tbody').append(basic_add_new_html);

    if (GLOBAL_ACTION == "transaction_types_upload") {
        $(".class_del_checkbox").prop("hidden", false);
    }
    table_sort_filter_popup('id_popup_table');
}



//**********************************
function read_sequence() {
    rendered_sequence_array = [];
    sequence_remove_array = [];
    $.each(rendered_transaction_types_data, function (i, value) {
        sequence_remove_array.push(value.sequence)
    });

    $.each(rendered_sequence, function (i, item) {
        rendered_sequence_array.push(item.sequence)
    });
    console.log(rendered_sequence_array);
}

//*************************************


read_sequence()
function eliminate_used_sequence() {
    sequence_dropdown = '';


    $.each(rendered_sequence_array, function (i, item) {
        if (sequence_remove_array.includes(item)) {
            rendered_sequence_array = $.grep(rendered_sequence_array, function (value) {
                return value != item;
            });
        }
    });

    $("#id_popup_table TBODY TR").each(function () {
        var row = $(this);
        sequence_popup = row.find("TD").eq(4).find("select option:selected").val();
        rendered_sequence_array = $.grep(rendered_sequence_array, function (item) {
            return item != sequence_popup;
        });

    })
    console.log("rendered_sequence_array",rendered_sequence_array);
    $.each(rendered_sequence_array, function (i, value) {
        sequence_dropdown += '<option value="' + value + '">' + value + '</option>'

    });
    console.log("sequence_dropdown",sequence_dropdown)


}

// on click copy icon display the selected checkbox data
function onclick_copy_button() {
    GLOBAL_ACTION = "COPY"
    onclick_copy_update_button("copy")
    document.getElementById("id_del_add_button").style.display = "block";
}
//***********************************
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
    $("#id_error_msg_transaction_types_code").prop("hidden", true);
    $("#id_error_msg_transaction_types_name").prop("hidden", true);
    $("#id_error_msg_transaction_types_length").prop("hidden", true);
    $("#id_check_error_messages").prop("hidden", true);
    $("#id_check_success_messages").prop("hidden", true);
    $("#id_check_special_character_messages").prop("hidden", true)
    $("#id_check_data").prop("hidden", true);
    sequence_dropdown = '';
    read_sequence()
    $('#id_popup_table').DataTable().destroy();


});



function display_error_message(error_message){

    $('#error_message').text(error_message);
   
    document.getElementById("error_message").style.color = "Red";
    $("#error_msg_id").css("display", "block")
    $('#id_save_confirm_popup').modal('hide');
    $('#myModal').modal('show');

}
//******************************************************

function delete_duplicate() {
    $('#id_popup_table').DataTable().destroy();
    var transaction_types_code_check = new Array
    $("#id_popup_table TBODY TR").each(function () {
        var row = $(this);

        //*************** reading data from the pop-up ***************
        transaction_type = row.find("TD").eq(2).find('input[type="text"]').val().toUpperCase();


        if (transaction_types_code_check.includes(country_code)) {
            $(row).remove();
        }

        transaction_types_code_check.push(transaction_type);


    })
    table_sort_filter_popup_pagination('id_popup_table')
    check_data()
}


// Functtion to hide and display save related popups

$('#save_id').click(function () {
    transaction_types_data = new Array();
    validate_add_attributes = [];
    $('#myModal').modal('hide');
     $("#id_popup_table TBODY TR").each(function() {
        var row = $(this);
        transaction_types = {};
        transaction_types.del_ind = row.find("TD").eq(7).find('input[type="checkbox"]').is(':checked');
        transaction_types.document_type = row.find("TD").eq(3).find("select option:selected").val();
        transaction_types.transaction_type = row.find("TD").eq(1).find('input[type="text"]').val();
        transaction_types.description = row.find("TD").eq(2).find('input[type="text"]').val();
        transaction_types.sequence = row.find("TD").eq(4).find("select option:selected").val();
        transaction_types.active_inactive = row.find("TD").eq(5).find('input[type="checkbox"]').is(':checked');
        transaction_types.guid = row.find("TD").eq(6).find('input[type="text"]').val();
        transaction_types.attribute_id ='FC_TRANS_TYPE'

        if (transaction_types == undefined) {
            transaction_types.transaction_type = row.find("TD").eq(2).find('input[type="text"]').val().toUpperCase();
        }
        if (transaction_types.guid == undefined){
            transaction_types.guid = ''
        }
        validate_add_attributes.push(transaction_types.transaction_type);
        transaction_types_data.push(transaction_types);
    });
    
    $('#id_save_confirm_popup').modal('show');
});


function cal(){
        price = document.getElementById('price').value;
        num = document.getElementById("num").value;
        totals = cal2(price,num);
        // alert(price);
        // alert(num);
        //alert(totals);

        document.getElementById("total").value = totals;

    }

function cal2(a,b){
    c = a * b;
    return c;
}

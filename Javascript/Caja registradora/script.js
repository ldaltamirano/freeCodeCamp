function checkCashRegister(price, cash, cid) {
    var conversion = {
        "ONE HUNDRED": 100,
        "TWENTY": 20,
        "TEN": 10,
        "FIVE": 5,
        "ONE": 1,
        "QUARTER": 0.25,
        "DIME": 0.10,
        "NICKEL": 0.05,
        "PENNY": 0.01,
    };

    let resultado = checkCashRegTickets(price, cash, cid);
    if (!resultado) {
        return { status: "INSUFFICIENT_FUNDS", change: [] }
    }

    let changeCash = cash - price;
    let ticketsCash = {};

    for (let i in conversion) {
        while (changeCash >= conversion[i]) {
            if (ticketsCash[i] == undefined) {
                ticketsCash[i] = 1;
            }
            else {
                ticketsCash[i] += 1;
            }
            changeCash -= conversion[i];
        }
    }
    updateCashRegister(cid, ticketsCash, conversion);

    if (!checkCashRegTickets(price, cash, cid)) {
        return { status: "CLOSED", change: [cid] }
    }
    
    let changeObj = statusOpen(ticketsCash);
    return { status: "OPEN", change: [changeObj] };
}



function statusOpen(ticketsCash) {
    let change;
    for (let i in ticketsCash) {
        if (change != undefined)
            change.splice(change.length, 0, [i, ticketsCash[i]]);
        else
            change = [i, ticketsCash[i]]
    }

    return change;
}

function updateCashRegister(cid, ticketsCash, conversion) {
    let cidCash = 0;
    for (let i in cid) {
        if (ticketsCash[cid[i][0]] != undefined)
            cid[i][1] = cid[i][1] - (ticketsCash[cid[i][0]] * conversion[cid[i][0]])
    }
    return cid;
}

function checkCashRegistCash(cid) {
    let cidCash = 0;
    for (let index = 0; index < cid.length; index++) {
        cidCash += cid[index][1];
    }
    return cidCash;
}

function checkCashRegTickets(price, cash, cid) {
    let cidTicket = 0;
    let cidCash = checkCashRegistCash(cid);
    for (let index = 0; index < cid.length; index++) {
        if (cid[index][1] == 0)
            cidTicket += 1;
    }
    let res = cidCash > 2 || cidCash == (cash - price) || cidTicket < 6;
    return res;
}

// checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);
// Aprobado:checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);
// checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]])
// Falló:checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]])
checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]])
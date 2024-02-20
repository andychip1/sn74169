module sn74169(
           input  [3:0] A,  
           input  U_DB, input CLK, input ENPB, input ENTB, input LOADB,
	   output reg [3:0] Q,
	   output reg RCOB
    );

 // loadb=0: load
 // NOR(enpb, entb) and U_DB: count up
 //                and !U_DB: count down

    always @(posedge CLK)
	RCOB=1;
	    
        if(!LOADB)
     		Q = A;
	else
		if (!ENPB && !ENTB)
			if(U_DB)
				Q=Q+1;
			else
				Q=Q-1;

    end

endmodule


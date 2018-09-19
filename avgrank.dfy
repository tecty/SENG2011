method avgrating(a: array<array<int>>, b : array<int>, n : int) returns (avg : int)
requires n > 0;
requires b.Length > 0;
ensures a.Length > 0;


{
    var b := new int[n];
    var k : int := 0;
    var cons : int := 0;
    var sum : int := 0;
    var i : int := 0;
    var j : int := 0; 
    while (i < b.Length)
    decreases b.Length-i;
	  invariant i<=b.Length;
    {
        k := b[i];
        while (j < a.Length)
        decreases a.Length-i;
	      invariant j<=a.Length;
        invariant k < n;
        {
            b := a[j];
            sum := sum + b[k];
            j := j+1;
        }
        i := i+1;
    }

    avg := sum / a.Length;
}
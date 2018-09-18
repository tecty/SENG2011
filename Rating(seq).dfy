// a is the sequence of parameters that involves in this particular post
// n is the number of total parameters
// b returns an array with scores corresponding to all parameters, while the involved ones will equal to score and the rest will equal to zero
method Rating(a:seq<int>, n:int, score:int) returns (b:array<int>)
	requires n > 0;
	ensures b.Length == n;
	ensures forall k :: 0<=k<b.Length && (k in a) ==> b[k] == score;
	ensures forall k :: 0<=k<b.Length && !(k in a) ==> b[k] == 0;
{
	b := new int[n];
	var i:int := 0;
	
	while (i < b.Length)
		decreases b.Length-i;
		invariant i<=b.Length;
		invariant forall k :: 0<=k<i && !(k in a) ==> b[k] == 0;
		invariant forall k :: 0<=k<i && k in a ==> b[k] == score;
	{
		if (i in a)
		{
			b[i] := score;
		}
		else
		{
			b[i] := 0;
		}
		i := i+1;
	}
}
method filter(a:array<int>, key:int) returns (b:seq<int>)
	ensures |b| <= a.Length;

	// the elements of b[0..n] are equal to key
	ensures forall k :: 0 <= k < |b| ==> b[k] == key;  
	// the elements of b[0..n] come from a
	ensures forall j :: 0 <= j < |b| ==> b[j] in a[0..]; 
	// every key element of a is in b[0..n]
	ensures forall k :: 0 <= k < a.Length && a[k] == key ==> a[k] in b;
{
	var i:int := 0;
	b := [];

	// copies in b all and only the key elements of a
	while (i < a.Length)
		invariant |b| <= i <= a.Length;
		// all the elements in b[0..n] are positive
		invariant forall k :: 0 <= k < |b|==> b[k] == key;
		// every element in b[0..n] occurs in a[0..i]
		invariant forall j:: 0 <= j < |b| ==> b[j] in a[0..i];
		// every positive element of a[0..i] occurrs in b[0..n]
		invariant forall k :: 0 <= k < i && a[k]==key ==> a[k] in b;
		decreases a.Length-i;
	{
		if (a[i] == key) 
		{ 
			b := b + [a[i]];
		}
		i := i + 1;
	}
}

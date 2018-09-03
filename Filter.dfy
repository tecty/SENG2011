method Filter(a:array<int>, key:int) returns (b:array<int>, n:int)
	ensures n <= a.Length;
	ensures b.Length == a.Length;

	// the elements of b[0..n] are equal to key
	ensures forall k :: 0 <= k < n ==> b[k] == key;  
	// the elements of b[0..n] come from a
	ensures forall j :: 0 <= j < n ==> b[j] in a[0..]; 
	// every key element of a is in b[0..n]
	ensures forall k :: 0 <= k < a.Length && a[k] == key ==> exists j :: 0 <= j < n && b[j] == a[k];
{
	var i:int := 0;
	n := 0;
	b := new int[a.Length];

	// copies in b all and only the key elements of a
	while (i < a.Length)
		invariant n <= i <= a.Length;
		invariant n <= b.Length;
		// all the elements in b[0..n] are positive
		invariant forall k :: 0 <= k < n ==> b[k] == key;
		// every element in b[0..n] occurs in a[0..i]
		invariant forall j:: 0 <= j < n ==> b[j] in a[0..i];
		// every positive element of a[0..i] occurrs in b[0..n]
		invariant forall k :: 0 <= k < i && a[k]==key ==> exists j:: 0 <= j < n && b[j] == a[k];
		decreases a.Length-i;
	{
		if (a[i] == key) 
		{ 
			b[n] := a[i];
			n := n + 1;
		}
		i := i + 1;
	}
}

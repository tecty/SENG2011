lemma  MutisetAddingLemma(a: array<int>,l:int, m: int, u:int)
requires 0<=l<=m<=u<a.Length
ensures multiset(a[l..m]) + multiset(a[m..u+1]) == multiset(a[l..u+1])
{
    assert a[l..m] + a[m..u+1] == a[l..u+1];
}

method MergeSort(a1:array<int>) returns (a:array<int>)
  requires a1 != null && a1.Length > 0;
  ensures a != null;
  ensures forall k:: forall l:: 0 <= k < l < a.Length ==> a[k] <= a[l];
{
  a := mergesort(a1, 0, a1.Length-1);
  return;
}

method mergesort(a1:array<int>, l:int, u:int) returns (a:array<int>)
  requires a1 != null && a1.Length > 0;
  requires 0 <= l <= u < a1.Length;
 
  ensures a != null;
  ensures a.Length == a1.Length;
  ensures forall q:: forall r:: l <= q < r <= u ==> a[q] <= a[r];
  ensures forall q:: (0 <= q < l || u < q < a.Length) ==> a[q] == a1[q];
  ensures multiset(a[l..u+1]) == multiset(a1[l..u+1]);
  ensures a[0..l] == a1[0..l];
  ensures a[u+1..] == a1[u+1..];
  decreases u-l;
{
  a := new int[a1.Length];

    var o:= 0;
  while (o < a.Length)
    invariant a1.Length == a.Length
    invariant 0 <= o <= a1.Length
    invariant forall q:: (0 <= q < a.Length) ==> a1[q] == old(a1[q]);
    invariant forall k:: 0 <= k < o ==> a[k] == a1[k]
    invariant a1[0..o] == a[0..o]
  {
    a[o] := a1[o];
    o := o + 1;
  }

  if (l >= u)
  {
    return;
  }
  else
  {
    var m:int := (l + u) / 2;
    a := mergesort(a1, l, m);
    assert a[m+1..u+1] == a1[m+1..u+1];
    a := mergesort(a, m+1, u);
    assert multiset(a[l..m+1]) == multiset(a1[l..m+1]);
    assert multiset(a[m+1..u+1]) == multiset(a1[m+1..u+1]);
    MutisetAddingLemma(a,l,m+1,u);
    MutisetAddingLemma(a1,l,m+1,u);
    assert multiset(a[l..u+1]) == multiset(a1[l..u+1]);
    a := merge(a, l, m, u);
    return;
  }
}

method merge(a:array<int>, l:int, m:int, u:int) returns (buf:array<int>)
  requires a.Length > 0;
  requires 0 <= l <= m <= u < a.Length;
  requires forall q:: forall r:: l <= q < r <= m ==> a[q] <= a[r];
  requires forall q:: forall r:: m+1 <= q < r <= u ==> a[q] <= a[r];
  
  ensures a.Length == buf.Length;
  ensures multiset(buf[..]) == multiset(a[..]);
  ensures multiset(buf[l..u+1]) == multiset(a[l..u+1]);
  ensures forall q:: forall r:: l <= q < r <= u ==> buf[q] <= buf[r];
  ensures forall q:: (0 <= q < l || u < q < buf.Length) ==> buf[q] == a[q];
{
//   var a := new int[a.Length];
//   assume forall k:: 0 <= k < a.Length ==> a[k] == a[k];
  
  buf := new int[a.Length];
  var o:= 0;
  while (o < a.Length)
    invariant buf.Length == a.Length
    invariant 0 <= o <= a.Length
    invariant forall q:: (0 <= q < a.Length) ==> a[q] == old(a[q]);
    invariant forall k:: 0 <= k < o ==> a[k] == buf[k]
    invariant buf[0..o] == a[0..o]
  {
    buf[o] := a[o];
    o := o + 1;
  }
  assert forall k:: 0 <= k < a.Length ==> a[k] == buf[k];


  var i:int := l;
  var j:int := m + 1;
  var k:int := 0;
  while (k < u-l+1)
    invariant  forall k:: 0 <= k < a.Length ==> a[k] == a[k];
      
    invariant 0 <= k <= u-l+1; // k is in this buffer index
    invariant m+1 <= j <= u+1; // j is in the right place
    invariant l <= i <= m+1; // i is in the right place
    
    invariant (i-l) + (j-(m+1)) == k; // k aligns properly.
    invariant buf.Length == a.Length;
    invariant multiset(buf[l..l+k]) == multiset(a[l..i]) + multiset(a[m+1..j]);
    invariant buf[0..l] == a[0..l];
    invariant buf[u+1..] == a[u+1..];
    invariant forall q:: forall r:: l <= q < r < k+l ==>  buf[q] <= buf[r]; // buf is sorted in [0,k). Most important condition.
    invariant forall q:: forall r:: l <= q < l+k && (i <= r <= m || j <= r <= u) ==> buf[q] <= a[r];

  {
    if (i > m)
    {
      buf[l+k] := a[j];
      j := j + 1;
    }
    else if (j > u)
    {
      buf[l+k] := a[i];
      i := i + 1;
    }
    else if (a[i] <= a[j])
    {
      buf[l+k] := a[i];
      i := i + 1;
    }
    else
    {
      buf[l+k] := a[j];
      j := j + 1;
    }
    k := k + 1;
  }
  assert j == u+1;
  assert i == m+1;
  assert k==u-l+1;
//   assert multiset(buf[..buf.Length]) == multiset(a[l..i]) + multiset(a[m+1..j]);
//   assert buf[..buf.Length] == buf[..];
  assert multiset(buf[l..u+1]) == multiset(a[l..m+1]) + multiset(a[m+1..u+1]);
  assert a[l..m+1] + a[m+1..u+1] == a[l..u+1];
assert multiset(a[l..m+1]) + multiset(a[m+1..u+1]) == multiset(a[l..u+1]);
  assert  buf[0..l] + buf[l..u+1] + buf[u+1..] == buf[..];
    assert buf[0..l] == a[0..l];
    assert buf[u+1..] == a[u+1..];
  assert  a[0..l] + a[l..u+1] + a[u+1..] == a[..];

    assert multiset(buf[u+1..]) == multiset(a[u+1..]);
    assert multiset(buf[0..l]) == multiset(a[0..l]);
  assert multiset(buf[l..u+1]) == multiset(a[l..u+1]);
  assert multiset(buf[0..l]) + multiset(buf[l..u+1]) + multiset(buf[u+1..]) == multiset(buf[..]);
  assert multiset(a[0..l]) + multiset(a[l..u+1]) + multiset(a[u+1..]) == multiset(a[..]);
  assert multiset(buf[..]) == multiset(a[..]);

}







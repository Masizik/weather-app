$(document).ready(function(){
		$(".toggle").on("click",function(){
			var $this = $(this);
			$this.next().slideToggle();
			if($this.text() === "Less Details"){
				$this.text("More Details");
			}else{
			  $this.text("Less Detail");
			}
		})
	});